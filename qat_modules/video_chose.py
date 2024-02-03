import pyautogui
import time

def video_chose():
    pyautogui.moveTo(613, 265)
    time.sleep(1)
    pyautogui.rightClick(613, 265)
    time.sleep(1)
    pyautogui.press('left') 
    pyautogui.press('enter') 
    time.sleep(1)
    pyautogui.press('right')
    time.sleep(0.5)
    pyautogui.press('right')
    time.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  
    