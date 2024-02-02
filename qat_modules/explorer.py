import pyautogui
import time
from qat_modules.img_recog import find_and_click

def explorer():
    #find IE
    ex_path = r'C:\Users\zoltan\Desktop\Letoltes\WebDev\GUI_auto\images\explo.png'
    find_and_click(ex_path)
    time.sleep(2)

    #open new tab
    pyautogui.hotkey('ctrl', 't')

  


