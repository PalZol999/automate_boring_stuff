import pyautogui

def find_and_click(img_path):
    try:
        location = pyautogui.locateOnScreen(img_path, confidence=0.8)
        
        if location is not None:
            x, y = pyautogui.center(location)
            pyautogui.click(x, y)
            print(f"Clicked on the image at ({x}, {y})")
        else:
            print("Image not found on the screen.")

    except Exception as e:
        print(f"Error: {e}")

