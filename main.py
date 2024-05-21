import pyautogui
import cv2
import os
import time

# Path to the assets folder containing the screenshots of all buttons
assets_path = './assets/de/'
location = None


# Function to locate an image on the screen and click it
def click_image(image_path, confidence=0.8):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
    except pyautogui.ImageNotFoundException:
        return False

    if location:
        pyautogui.click(location)
        return True
    return False


# Function to remove a friend
def remove_friend(location, delay):
    pyautogui.click(location)

    time.sleep(delay)  # Wait for the options to load

    # Find and click the "More options" button
    if not click_image(os.path.join(assets_path, 'more.png')):
        print("More options button not found.")
        return False

    time.sleep(delay)  # Wait for the options to load

    # Find and click the "Remove Friend" button
    if not click_image(os.path.join(assets_path, 'remove.png')):
        print("Remove Friend button not found.")
        return False

    time.sleep(delay)  # Wait for the confirmation dialog to load

    # Find and click the "Remove Friend" button again to confirm
    if not click_image(os.path.join(assets_path, 'remove.png')):
        print("Confirm Remove Friend button not found.")
        return False

    time.sleep(delay)  # Wait for the friend to be removed

    # Close the two windows by finding the X of the window
    if not click_image(os.path.join(assets_path, 'close.png')):
        print("Close window button not found.")
        return False

    time.sleep(delay)  # Wait for the window to close

    # Close the second window
    if not click_image(os.path.join(assets_path, 'close.png')):
        print("Close window button not found.")
        return False

    time.sleep(delay)  # Wait for the window to close

    return True


if __name__ == "__main__":
    delay = float(input("Enter the delay in seconds: "))

    time.sleep(5)
    print("Finding the initial location...")
    location = pyautogui.locateCenterOnScreen(os.path.join(assets_path, 'friend.png'), confidence=0.8)
    if not location:
        print("Initial location not found.")
        exit(1)

    while True:
        remove_friend(location, delay)
        print(f"Friend removed. Next friend in {delay} second.")
        time.sleep(delay)
