#! python3
import pyautogui
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
    
    #chose the video
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
    
    #open the IJ
    ij_path = r'C:\Users\zoltan\Desktop\Letoltes\WebDev\GUI_auto\images\ij.png'
    find_and_click(ij_path)
    time.sleep(6)
    
    #click on terminal
    pyautogui.moveTo(31, 860)
    time.sleep(1)
    pyautogui.click(31, 860)
    time.sleep(2)
    
# Construct the command
    pyautogui.typewrite('java -cp build/libs/system-tests.jar com.microsoft.playwright.CLI show-trace reports/traces/')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.typewrite('.zip')
    time.sleep(0.5)
    pyautogui.press('enter')
    
    
playwrite()
