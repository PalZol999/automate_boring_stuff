import pyautogui
import time

def gradel_config():
    #find and click gradle
    pyautogui.moveTo(1380, 26)
    time.sleep(1)
    pyautogui.click(1380, 26)
    time.sleep(1)

    #find and click the Edit config
    pyautogui.moveTo(1458, 158, duration=1)
    time.sleep(1)
    pyautogui.click(1458, 158)
    time.sleep(1)