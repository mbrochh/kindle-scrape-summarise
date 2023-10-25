---
theme: default
title: Summarising books with ChatGPT, Python and Logseq
background: images/cover.png
class: 'text-center'
highlighter: shiki
lineNumbers: true
drawings:
  persist: true
transition: fade-out
css: unocss
---

<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<div class="text-left relative">
    <div class="z-90 text-lg">Summarising books with ChatGPT, Python and Logseq</div>
    <div class="text-sm mt-0">by <a href="https://twitter.com/mbrochh" target="_blank">Martin Brochhaus</a></div>
    <div class="text-sm mt-1">slides: <a href="https://bit.ly/pugs-kindle" target="_blank">https://bit.ly/pugs-kindle</a></div>
</div>

---
clicks: 3
---

# About PUGS

<ul>
    <li v-click="1">
        PUGS stands for <span class="text-red">Python User Group Singapore</span>
        <ul>
            <li>registered non-profit society, run by volunteers</li>
            <li>was created to organize <a class="text-red" href="https://pycon.sg" target="_blank">PyCon Singapore</a></li>
        </ul>
    </li>
    <li v-click="2">
        Visit <a class="text-red" href="https://pugs.org.sg/membership/" target="_blank">https://pugs.org.sg/membership/</a> to become a member
    </li>
    <li v-click="3">
        Monthly meetups at <a class="text-red" href="https://www.meetup.com/singapore-python-user-group/" target="_blank">https://www.meetup.com/singapore-python-user-group/</a>
    </li>
</ul>

<div class="grid grid-cols-3 gap-4 mt-4 max-h-[220px] overflow-hidden">
  <div v-click="1"><img src="/images/pycon.png" /></div>
  <div v-click="2"><img src="/images/membership.png" /></div>
  <div v-click="3"><img src="/images/meetup.png" /></div>
</div>

---

# About me

- Martin Brochhaus
- CTO of [theartling.com](https://theartling.com/en/)
- Committee member of PUGS
- Twitter: [@mbrochh](https://twitter.com/mbrochh)

<div class="grid grid-cols-2 gap-4 mt-4 max-h-[300px] overflow-hidden">
  <div><img src="/images/theartling.png" class="max-h-[300px] mx-auto" /></div>
  <div><img src="/images/twitter.png" class="max-h-[300px] mx-auto" /></div>
</div>

---

# Part 1: Summarising Youtube Videos With Whisper & ChatGPT

- Slides for the first talk [here](https://mbrochh.github.io/whisper-youtube-transcribe/1)
- Video for the first talk [here](https://www.youtube.com/watch?v=t5eVAtavoQ8&t=76s)
- Step 1: **Download** the **audio** of a Youtube video
- Step 2: **Transcribe** the audio into a textfile with **Whisper**
- Step 3: Turn the text into **chunks** of no more than ~14000 words
- Step 4: Send each chunk to **OpenAI's API** and request a **summary**

---

# Today's Project: Summarizing Books with ChatGPT and pyTesseract

- Step 1: **Take screenshots** of the Kindle pages
- Step 2: Use **pyTesseract** to **extract the text** from the screenshots
- Step 3: **Chunk** the text by subchapter
- Step 4: **Ask ChatGPT** for a summary
- Step 5: **Format** the summary for **Logseq**

<div class="flex gap-4 mt-4 max-h-[300px] overflow-hidden">
  <div><img src="/images/kindle_screenshot.png" class="max-h-[300px] mx-auto" /></div>
  <div><img src="/images/logseq2.png" class="max-h-[300px] mx-auto" /></div>
</div>

---

# Step 1: Taking Screenshots of Kindle Pages

- We will use Python's `Pillow` library to take screenshots
- We will make sure that only the part that contains the actual text is part of the screenshot

<img src="/images/kindle_screenshot.png" class="max-h-[300px] mx-auto mt-4" />

---

# Step 2: Using Python Tesseract for OCR

- We will use [pytesseract](https://github.com/madmaze/pytesseract) to extract the text from the screenshot

<img src="/images/ocr_output.png" class="max-h-[300px] mx-auto mt-4" />

---

# Step 3: Chunking Text by Subchapter

- We will find a way to extract the text that ranges from one subchapter title to the next
- Our goal is to turn the book text into a data structure like shown below

<div class="flex gap-4 mt-4 max-h-[300px] overflow-hidden">
  <div><img src="/images/subchapter1.png" class="max-h-[300px] mx-auto" /></div>
  <div><img src="/images/subchapter2.png" class="max-h-[300px] mx-auto" /></div>
  <div><img src="/images/datastructure.png" class="max-h-[100px] mx-auto" /></div>
</div>

---

# Step 4: Asking ChatGPT for a Summary

- We will create a prompt for ChatGPT
- When a subchapter is very long, it might have many chunks
- We will still always send the book title and subchapter title to ChatGPT

```python
PROMPT = """
Your task is as follows:

- Create a bullet point summary of the following text. 
- Do not just list the general topic, but the actual facts that were shared.
- Use '- ' for bullet points:
- Keep in mind the following context about the text

CONTEXT:
Book title: {book_title}
Chapter title: {chapter_title}
Subchapter title: {subchapter_title}

TEXT TO SUMMARISE:
{chunk}
"""
```

---

# Step 5: Formatting ChatGPTs Output for Logseq

- Finally, we will make sure that the output can be pasted right into [Logseq](https://logseq.com/)
- For this, we will have to make sure that the indentation is correct for the chapters, subchapters, and summary bulletpoints

<div class="flex gap-4 mt-4 max-h-[300px] overflow-hidden">
  <div><img src="/images/logseq1.png" class="max-h-[300px] mx-auto" /></div>
  <div><img src="/images/logseq2.png" class="max-h-[300px] mx-auto" /></div>
</div>

---

# Let's Get Started!

- :-)

---

# Creating a project folder

- Whenever you start a new Python project, you will want to create a new folder for it

```bash
mkdir -p ~/Projects/kindle_scrape/kindle_scrape

# Let's `cd` into the newly created folder
cd ~/Projects/kindle_scrape
```

- NOTE: the `mkdir` command stands for "make directory"
- NOTE: the `cd` command stands for "change directory"

---

# Creating the project files

```bash
cd ~/Projects/kindle_scrape

# Now create a few files that we will need later:
touch .gitignore
touch requirements.txt
touch kindle_scrape/__init__.py
touch kindle_scrape/screenshot.py
touch kindle_scrape/scrape.py
touch kindle_scrape/subchapters.py
touch kindle_scrape/summarise.py
touch kindle_scrape/local_settings.py
touch kindle_scrape/outline.py

# We will also need a few folders for all the files that our tool will generate:
mkdir -p files/screenshots
mkdir -p files/texts
mkdir -p files/summaries
```

- NOTE: the `touch` command creates an empty file

---

# Double-checking

- When you run `tree . -a`, your file structure should look like this:

```bash
.
├── .gitignore
├── files
│   ├── screenshots
│   ├── summaries
│   └── texts
├── kindle_scrape
│   ├── __init__.py
│   ├── local_settings.py
│   ├── outline.py
│   ├── scrape.py
│   ├── screenshot.py
│   ├── subchapters.py
│   └── summarise.py
└── requirements.txt


5 directories, 9 files
```

---

# The `.gitignore` file

- Put the following code into the `.gitignore` file:

```bash
local_settings.py
outline.py
files/
__pycache__/
.DS_Store
```

---

# The `local_settings.py` file

- Put the following code into the `local_settings.py` file:

```python
OPENAI_API_KEY = "YOUR OPENAI API KEY HERE"
FILES_PATH = "/Users/YOUR USERNAME HERE/Projects/kindle_scrape/files"
RECT_TOP_LEFT = (1045 * 2, 69 * 2)
RECT_BOTTOM_RIGHT = (1899 * 2, 1391 * 2)
```

- You can get your API key [here](https://platform.openai.com/account/api-keys)
- This is considered secret information, which is why we have this file in `.gitignore`
- Never share this key with anyone or they can use your OpenAI credits
- Consider storing this key in a password manager because you won't be able to see it again once it has been created

---

# The `requirements.txt` file

- We will need a few Python libraries throughout these slides
- To make things easier, we will just install them all at once
- Put the following code into the `requirements.txt` file:

```bash
openai==0.27.4
spacy==3.5.2
tiktoken==0.3.1
requests==2.28.2
Pillow==10.0.0
pyobjc==9.2
pytesseract==0.3.10
```


---

# The Virtual Environment

- Make sure that you have [pyenv](https://github.com/pyenv/pyenv) installed
- Make sure that you have the [pyenv-virtualenv plugin](https://github.com/pyenv/pyenv-virtualenv) installed
- Now you can `pip install` all the modules in the `requirements.txt` file

```bash
cd ~/Projects/kindle_scrape
pyenv virtualenv kindle_scrape
pyenv activate kindle_scrape
pip install -r requirements.txt
```

---
layout: two-cols
---

# The `screenshot.py` File

- We can use the `ImageGrab` class function from the `PIL` library to take a screenshot
- We can use the `crop()` function to crop the screenshot to the rectangle that we want
- We can execute this file via `python -m kindle_scrape.screenshot`

::right::

<H1>&nbsp;</H1>

```python {2,6,13}
import time
from PIL import ImageGrab
from .local_settings import RECT_BOTTOM_RIGHT, RECT_TOP_LEFT, FILES_PATH

def take_screenshot():
    screenshot = ImageGrab.grab()

    # Define rectangle coordinates
    top_left = RECT_TOP_LEFT
    bottom_right = RECT_BOTTOM_RIGHT

    # Crop the screenshot to the given rectangle
    screenshot = screenshot.crop((*top_left, *bottom_right))

    # Generate unique filename based on current time
    filename = f"{FILES_PATH}/screenshots/{int(time.time())}.png"
    
    screenshot.save(filename)

if __name__ == "__main__":
    take_screenshot()
```

---

# Automator

- On MacOS, you can use the Automator app to create a shortcut that will run the `screenshot.py` file

<div class="flex gap-4 mt-4 max-h-[300px] overflow-hidden">
  <div><img src="/images/automator.png" class="max-h-[300px] mx-auto" /></div>
  <div><img src="/images/shortcut.png" class="max-h-[300px] mx-auto" /></div>
</div>

---
layout: two-cols
---

# The `scrape.py` File

- All the magic happens in the `image_to_string()` function from `pytesseract`
- The entire rest of the code is just looping over all the images on the disk and then saving the final text file
- After we have taken some screenshots, we can execute this file via `python -m kindle_scrape.scrape`

::right::

<H1>&nbsp;</H1>

```python  {3,15} {maxHeight:'400px'}
import time
import os
import pytesseract

from .local_settings import FILES_PATH

def scrape_text():
    texts = []
    folder_path = os.path.join(FILES_PATH, 'screenshots')
    filenames = sorted(os.listdir(folder_path))
    total_files = len(filenames)
    for index, filename in enumerate(filenames):
        print(f'Processing file {index + 1} of {total_files}...')
        file_path = os.path.join(folder_path, filename)
        text = pytesseract.image_to_string(file_path)
        texts.append(text)

    filename = f'{int(time.time())}.txt'
    file_path = os.path.join(FILES_PATH, 'texts', filename)
    with open(file_path, 'w') as file:
        file.write('\n'.join(texts))
    return filename

if __name__ == '__main__':
    result = scrape_text()
    print(f'Output file: {result}')
```

--- 

# The `outline.py` File

- Sadly, there is no easy way to detect which text in the extracted text file is a chapter or subchapter headline
- pyTesseract cannot distinguish between different font sizes
- as a crutch, we will manually take note of the chapter and subchapter titles as we read the book

```python
outline = {
    'book': 'The Ethics of Money Production',
    'chapter': 'Introduction',
    'subchapters': [
        '1. MONEY PRODUCTION AND JUSTICE',
        '2. REMARKS ABOUT RELEVANT LITERATURE'
    ]
}
```

---

# Asking ChatGPT for Help...

<img src="/images/chapters_gpt_1.png" class="max-h-[300px] mx-auto" />

<div class="grid grid-cols-2 gap-4 mt-4 overflow-hidden">
  <div><img src="/images/outline.png" /></div>
  <div><img src="/images/ocr_output.png" /></div>
</div>

---

# Asking ChatGPT for Help...

<img src="/images/chapters_gpt_2.png" class="max-h-[400px] mx-auto" />

---

# ChatGPT Too Smart! Explain it Like I'm 5...

<img src="/images/ask_gpt1.png" class="max-h-[400px] mx-auto" />

---

# ChatGPT Too Smart! Explain it Like I'm 5...

<img src="/images/ask_gpt2.png" class="max-h-[400px] mx-auto" />

---

# The Idea, Visualised

- We want to turn the text into one big string
- Then we want to slice the string at the subchapter titles
- The regex for this slice looks like `Chapter 1 Title|Chapter 2 Title`

<div class="flex gap-4 mt-4">
  <div><img class="max-h-[500px]" src="/images/re_example1.png" /></div>
  <div><img src="/images/re_example2.png" /></div>
  <div><img src="/images/re_example3.png" /></div>
</div>

---
layout: two-cols
---

# The `subchapters.py` File

- First, we turn the entire book text into one giant long string
- Then we use ChatGPT's amazing idea to use `re.split()` to split the text into chunks based on the subchapter titles
- We can execute this file via `python -m kindle_scrape.subchapters FILENAME.txt`

::right::

<h1>&nbsp;</h1>

```python {15,17} {maxHeight:'350px'}
import re
import sys
from .local_settings import FILES_PATH
from .outline import outline

def get_subchapter_contents(filepath):
    with open(filepath, "r") as f:
        content = f.readlines()

    # Normalize the content by removing newlines and extra spaces
    content_normalized = " ".join([line.strip() for line in content])
    # Remove extra spaces
    content_normalized = re.sub(" +", " ", content_normalized)
    # Create a regex pattern that matches any of the subchapters
    pattern = "|".join(map(re.escape, outline["subchapters"]))
    # Splitting the string based on the chapter titles
    subchapters = re.split(pattern, content_normalized)
    # Filter out any empty chunks
    subchapters = [subchapter.strip() for subchapter in subchapters if subchapter.strip()]

    expected_subchapter_count = len(outline["subchapters"])
    found_subchapters = len(subchapters)
    if found_subchapters != expected_subchapter_count:
        raise Exception(
            f"ERROR: Expected {expected_subchapter_count} subchapters but found {found_subchapters}"  # noqa
        )

    return subchapters


if __name__ == "__main__":
    filename = sys.argv[1]
    filepath = f"{FILES_PATH}/texts/{filename}"
    subchapters = get_subchapter_contents(filepath)
    for subchapter in subchapters:
        print(subchapter[:100], '...')
```

---

# Understanding Tokens...

<img class="max-h-[400px]" src="/images/prompt_calc.png" />

---

# Understanding Chunking...

<img class="max-h-[400px]" src="/images/chunks1.png" />

---

# Understanding Chunking...

<img class="max-h-[400px]" src="/images/chunks2.png" />

---

# Understanding Chunking...

<img class="max-h-[400px]" src="/images/chunks3.png" />

---

# Understanding Chunking...

<img class="max-h-[400px]" src="/images/chunks4.png" />

---

# Download en_core_web_sm

- In the terminal, run `python -m spacy download en_core_web_sm`
- You can learn more about this [here](https://spacy.io/models/en)

---

# The `summarise.py` File

- This file does quite a lot
- It will call the `get_subchapter_contents()` from the `subchapters.py` file
- It will then split the subchapters into chunks of no more than ~14000 words
- It will call OpenAI to get a summary for each chunk
- It will save the summaries to a text file in a nice format
- We can execute this via `python -m kindle_scrape.summarise FILENAME.txt`


```python {all} {style:'max-height:250px;overflow:scroll;'}
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

# see https://platform.openai.com/docs/models/gpt-3-5
MODEL = "gpt-3.5-turbo-16k"
MODEL_MAX_TOKENS = 16384
RESPONSE_TOKENS = 4000


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
    enc = tiktoken.encoding_for_model(MODEL)
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
    prompt_tokens = count_tokens(prompt)

    print("Sending prompt to OpenAI API...")


    # see https://platform.openai.com/docs/api-reference/chat/create
    result = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=MODEL_MAX_TOKENS - prompt_tokens - 10,
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
        chunks = split_text(
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
```

---

# Tadaaaa!

<div class="flex gap-4 mt-4 max-h-[300px] overflow-hidden">
  <div><img src="/images/logseq1.png" class="max-h-[300px] mx-auto" /></div>
  <div><img src="/images/logseq2.png" class="max-h-[300px] mx-auto" /></div>
</div>

---

# Oh My God, What Have We Done?!

<img src="/images/comic.jpg" class="max-h-[300px] mx-auto" />
<p class="text-center text-xs">source: <a href="https://marketoonist.com/2023/03/ai-written-ai-read.html">marketoonist</a></p>

---

# Thank you for your attention!

- Join the Python User Group: [https://pugs.org.sg/membership](https://pugs.org.sg/membership)
- Find the slides at [https://bit.ly/pugs-kindle](https://bit.ly/pugs-kindle)

---
layout: end
---