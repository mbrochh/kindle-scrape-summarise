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