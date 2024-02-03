import pyautogui
import time

def path_to_address():
    pyautogui.typewrite(r"\\wsl.localhost\Ubuntu\home\zoltan\code\system-tests\reports\traces")
    pyautogui.press('enter') 
    pyautogui.moveTo(1247, 117)
    time.sleep(1)
    pyautogui.click(1247, 117)
    time.sleep(1)