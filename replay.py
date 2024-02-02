#! python3
import pyautogui
import sys
import time
from playwrite import playwrite
from qat_modules.img_recog import find_and_click

#find IE
ex_path = r'C:\Users\zoltan\Desktop\Letoltes\WebDev\GUI_auto\images\explo.png'
find_and_click(ex_path)
time.sleep(2)

#open new tab
pyautogui.keyDown('ctrl')
pyautogui.press('t')
pyautogui.keyUp('ctrl')

#open collab page
if len(sys.argv) > 1:
    input_text= sys.argv[1]
else:
    input_text = '540' 
pyautogui.moveTo(803, 61)
time.sleep(1)
pyautogui.click(803, 61)
pyautogui.typewrite(f'https://collab.twint.ch/jira/browse/QAT-{input_text}')
time.sleep(1)
pyautogui.press('enter') 

playwrite()


