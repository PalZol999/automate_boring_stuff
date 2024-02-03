import pyautogui
import time
from qat_modules.img_recog import find_and_click
from qat_modules.video_chose import video_chose
from qat_modules.path_to_address import path_to_address

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
    path_to_address()
    
    #chose the video
    video_chose()
    
    #open the IJ
    ij_path = r'C:\Users\zoltan\Desktop\Letoltes\WebDev\GUI_auto\images\ij.png'
    find_and_click(ij_path)
    time.sleep(8)
    
    #click on terminal
    pyautogui.moveTo(31, 860)
    time.sleep(1)
    pyautogui.click(31, 860)
    time.sleep(2)
    
# Terminal path
    pyautogui.typewrite('java -cp build/libs/system-tests.jar com.microsoft.playwright.CLI show-trace reports/traces/')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.typewrite('.zip')
    time.sleep(0.5)
    pyautogui.press('enter')
    
    
playwrite()