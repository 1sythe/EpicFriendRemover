import pyautogui
import os
import time
import keyboard


# Path to the assets folder containing the screenshots of all buttons
assets_path = './assets/{lang}/'
location = None


def get_initial_location():
    print("Hover over the last friend and press F5 to set the initial location.")
    while True:
        if keyboard.is_pressed('f5'):
            return pyautogui.position()
        time.sleep(0.1)


# Function to locate an image on the screen and click it
def click_image(image_path, confidence=0.8):
    try:
        location = pyautogui.locateCenterOnScreen(image_path.format(lang=language), confidence=confidence)
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
    # print the ascii art
    with open("assets/ascii.txt", "r") as f:
        print(f.read())

    print("EpicGames Friend Remover v0.2 by myenv")
    input("Please open the Epic Games Launcher and navigate to the Friends tab. "
          "Make sure the window is maximized. [Press Enter]")
    input("Scroll to the bottom of your friend list. [Press Enter]")

    delay = float(input("Enter the delay between actions in seconds: "
                        "(low values may cause errors, recommended: 0.5-2)"))
    language = input("Enter the language of the Epic Games Launcher (de/en): ")

    location = get_initial_location()

    # Clear console
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Configuration complete.")
    input("Press enter to start the process. Make sure the Epic Games Launcher is in the foreground. "
          "You have 5 seconds.")

    time.sleep(5)

    while True:
        remove_friend(location, delay)
        print(f"Friend removed. Next friend in {delay} second.")
        time.sleep(delay)

