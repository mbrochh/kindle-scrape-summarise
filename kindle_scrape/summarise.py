import sys
import re
import tiktoken
import openai
import spacy

from .local_settings import FILES_PATH, OPENAI_API_KEY
from .subchapters import get_subchapter_contents
from .outline import outline

PROMPT = """
Your task is as follows:

- Create a bullet point summary of the following text. 
- Do not just list the general topic, but the actual facts that were shared.
- Use '- ' for bullet points:
- Keep in mind the following context about the text
- Do not mention the CONTEXT in your summary

CONTEXT:
Book title: {book_title}
Chapter title: {chapter_title}
Subchapter title: {subchapter_title}

TEXT TO SUMMARIZE:
{chunk}
"""

# see https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo
MODEL = "gpt-4-0125-preview"
ENCODING = "cl100k_base"
MODEL_MAX_TOKENS = 30000
RESPONSE_TOKENS = 2000


def slugify(value):
    """
    Normalizes a string: converts to lowercase, removes non-alpha characters,
    and converts dashes and spaces to underscores.

    """
    # Remove non-ASCII characters
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    # Turn remaining whitespace and dashes into underscores
    value = re.sub(r"[-\s]+", "_", value)
    return value


def count_tokens(text):
    """Count tokens in a text string using tiktoken."""
    enc = tiktoken.get_encoding(ENCODING)
    tokens = enc.encode(text)
    token_count = len(tokens)
    return token_count


def get_summary_from_openai(
    book_title=None,
    chapter_title=None,
    subchapter_title=None,
    chunk=None,
):
    """
    Calls OpenAI API to summarize a chunk of text.

    """
    openai.api_key = OPENAI_API_KEY
    prompt = PROMPT.format(
        book_title=book_title,
        chapter_title=chapter_title,
        subchapter_title=subchapter_title,
        chunk=chunk,
    )

    print("Sending prompt to OpenAI API...")

    # see https://platform.openai.com/docs/api-reference/chat/create
    result = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=RESPONSE_TOKENS,
        temperature=0,
        n=1,
        stream=False,
    )
    return result


def split_text(
    book_title=None,
    chapter_title=None,
    subchapter_title=None,
    subchapter_content=None,
):
    # with book and chapter titles filled in, how many tokens does the prompt
    # take up so far?
    prompt_tokens = count_tokens(
        PROMPT.format(
            book_title=book_title,
            chapter_title=chapter_title,
            subchapter_title=subchapter_title,
            chunk="",
        )
    )
    # now we can calculate how many tokens we have left for the text
    max_tokens = MODEL_MAX_TOKENS - prompt_tokens - RESPONSE_TOKENS

    # we can load a machine learning model here that can detect English
    # sentences
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("sentencizer")

    # here we use the ML model to split the text into a document that contains
    # all the sentences
    doc = nlp(
        subchapter_content,
        disable=["tagger", "parser", "ner", "lemmatizer", "textcat"],
    )

    chunks = []
    current_chunk = []

    # doc.sents stands for "document sentences"
    for sent in doc.sents:
        sent_text = sent.text.strip()  # this is one sentence
        sent_tokens = count_tokens(sent_text)

        if (
            sum([count_tokens(chunk) for chunk in current_chunk]) + sent_tokens
            > max_tokens
        ):
            # the sentence would make the chunk too big, so start a new chunk
            chunks.append(" ".join(current_chunk))
            current_chunk = [sent_text]
        else:
            # the sentence still fits into the current chunk
            current_chunk.append(sent_text)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    total_token_count = sum([count_tokens(chunk) for chunk in chunks])
    return chunks, total_token_count


def save_summaries(summaries=None):
    book_title = outline["book"]
    chapter_title = outline["chapter"]
    filename = slugify(book_title + "_chapter_" + chapter_title)

    with open(f"{FILES_PATH}/summaries/{filename}.txt", "w") as f:
        f.write(f"- # {chapter_title}\n")
        for subchapter_title in summaries.keys():
            f.write(f"  - ## {subchapter_title}\n")
            content = summaries[subchapter_title]
            lines = ['    ' + line.strip() + '\n' for line in content.split('\n') if line.strip()]
            f.writelines(lines)


if __name__ == "__main__":
    filename = sys.argv[1]
    filepath = f"{FILES_PATH}/texts/{filename}"
    subchapters = get_subchapter_contents(filepath)

    summaries = {}
    book_title = outline["book"]
    chapter_title = outline["chapter"]

    for idx, content in enumerate(subchapters):
        subchapter_title = outline["subchapters"][idx]
        chunks, total_token_count = split_text(
            book_title=book_title,
            chapter_title=chapter_title,
            subchapter_title=subchapter_title,
            subchapter_content=content,
        )

        subchapter_summaries = ""
        for chunk in chunks:
            result = get_summary_from_openai(
                book_title=book_title,
                chapter_title=chapter_title,
                subchapter_title=subchapter_title,
                chunk=chunk,
            )
            subchapter_summaries += result["choices"][0]["message"]["content"] + "\n"

        summaries[subchapter_title] = subchapter_summaries

    save_summaries(summaries=summaries)