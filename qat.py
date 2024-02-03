#! python3
import sys
import pyautogui
import time
from qat_modules.img_recog import find_and_click
from qat_modules.apply_run import apply_run
from qat_modules.gradle_config import gradel_config
from qat_modules.branch_search import branch_search
from qat_modules.explorer import explorer

#open the IJ
ij_path = r'C:\Users\zoltan\Desktop\Letoltes\WebDev\GUI_auto\images\ij.png'
find_and_click(ij_path)
time.sleep(8)

#search the branch
branch_search()

#change the branch
if len(sys.argv) > 1:
    input_text = sys.argv[1]
else:
    # Default value if no argument is provided
    input_text = '540' 
pyautogui.moveTo(416, 70)
time.sleep(2)
pyautogui.click(416, 70)
pyautogui.typewrite(input_text)
time.sleep(1)
pyautogui.press('enter') 
time.sleep(2)
pyautogui.press('enter')

#incase of same branch
time.sleep(1)
pyautogui.press('esc')

#gradel config
gradel_config()

#find and change the QAT
pyautogui.moveTo(1108, 272)
time.sleep(1)
pyautogui.doubleClick(1108, 272)
time.sleep(1)
pyautogui.typewrite(input_text)
time.sleep(1)

# apply and run
apply_run()
time.sleep(5)

#open collab page
explorer()
pyautogui.moveTo(803, 61)
time.sleep(1)
pyautogui.click(803, 61)
pyautogui.typewrite(f'https://collab.twint.ch/jira/browse/QAT-{input_text}')
time.sleep(1)
pyautogui.press('enter') 


