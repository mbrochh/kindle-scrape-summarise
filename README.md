# Summarising books with ChatGPT, Python and Logseq

This is a talk that I presented for the Python User Group Singapore and the
National Library Board in October 2023.

You can find the slides [here](https://mbrochh.github.io/kindle-scrape-summarise/1)

You can find the vidoe [here](https://www.youtube.com/watch?v=Shex-VKNLuM)

This is part two of a three part series

1. [Introduction to ChatGPT, Copilot & Whisper](https://mbrochh.github.io/whisper-youtube-transcribe/1)
2. [Summarising books with ChatGPT, Python and Logseq](https://mbrochh.github.io/kindle-scrape-summarise/1)
3. [Talk to your notes with Logseq and ChatGPT](https://mbrochh.github.io/logseq-faiss-chatgpt/1)

## Running the slides

* `git checkout slides`
* Learn more about how to run and build the slides in the README.md in the slides branch

## Running the code

* clone this repo
* create a vrirtual environment for this repo
* run `pip install -r requirements.txt`
* run `cd kindle_scrape & cp local_settings.py.sample local_settings.py`
* fill in your values into the `local_settings.py` file
* open the Kindle App on your computer and maximise the app
* open your terminal and place it on top of your kindle app, shrink down the terminal window size so that it does not overlap with the kindle app
* in your terminal:
    * make sure that you `cd` into the cloned repo folder
    * run `python -m kindle_scrape.screenshot`
    * this should create a file in the `screenshots` folder
    * the screenshot will likely be cropped wrongly so that the whole book page is not visible
    * on MacOS, when you press `CMD + SHIFT + 4` the screenshot tool appears and shows the mouse coordinates
    * note down the coordinates of the top left and bottom right corner of the book page and fill them into the `local_settings.py` file
    * run `python -m kindle_scrape.screenshot` again and make sure that the entire book page is visible
* now keep reading your book and take one screenshot of every page
* when you are done reading with a few sub-chapters (or all sub-chapters of your current main chapter), fill in the `outline.py` file
* run `python -m kindle_scrape.scrape`
    * you should see a file like `1706327559.txt` in the `files/texts` folder
    * make sure that the very first line of that file is the first sub-chapter title
    * if you can see the main chapter title on the first line, delete that title
* run `python -m kindle_scrape.summarise`
    * you should see output like `Sending prompt to OpenAI API...`
    * there will be at least as many API calls as you have sub-chapters
    * if one sub-chapter has more than 30000 tokens of text, then there will be several API calls for that long sub-chapter
    * in the end, you will see a file in the `files/summaries` folder

NOTE: I know that it is a bit annoying that we have to fill out the `outline.py` file manually.
Unfortunately, I can't think of any other way to make pyTesseract aware that certain texts are 
titles and sub-titles and other texts are just normal content.

I guess in the near future we will not need OCR any more, we will just upload the entire book page
into a multi-modal LLM that can take in images and that LLM would probably understand the structure
of the book page and would be able to know what is a headline and what is a sub-headline and what is
normal content.