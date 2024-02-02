'''#! python3'''
import pyautogui
import sys
import time
from qat_modules.img_recog import find_and_click

def playwrite():
    
    #find the folder
    folder_path = r'C:\Users\zoltan\Desktop\Letoltes\WebDev\GUI_auto\images\folder.png'
    find_and_click(folder_path)
    time.sleep(2)
    
    #find the address bar
    pyautogui.moveTo(1388, 67)
    time.sleep(1)
    pyautogui.click(1388, 67)
    time.sleep(1)
    
    #add the path to address
    pyautogui.typewrite(r"\\wsl.localhost\Ubuntu\home\zoltan\code\system-tests\reports\traces")
    pyautogui.press('enter') 
    pyautogui.moveTo(1247, 117)
    time.sleep(1)
    pyautogui.click(1247, 117)
    time.sleep(1)
    
#playwrite()
