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