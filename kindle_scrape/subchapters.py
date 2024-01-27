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