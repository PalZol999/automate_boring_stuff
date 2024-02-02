import pyautogui
import time

def apply_run():
    # Apply
    pyautogui.moveTo(1398, 904)
    time.sleep(1)
    pyautogui.click(1398, 904)
    time.sleep(1)

    # Run
    pyautogui.moveTo(1041, 904)
    time.sleep(1)
    pyautogui.click(1041, 904)
