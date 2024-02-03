import pyautogui
import time
from qat_modules.img_recog import find_and_click

#find the folder
folder_path = r'C:\Users\zoltan\Desktop\Letoltes\WebDev\GUI_auto\images\folder.png'
find_and_click(folder_path)
time.sleep(2)

#find the movie folder and copy it
pyautogui.click(1000, 500)
pyautogui.moveTo(613, 265)
time.sleep(1)
pyautogui.click(613, 265)
time.sleep(1)
pyautogui.hotkey('ctrl', 'x')

#open the Old folder and add it
pyautogui.moveTo(437, 222)
time.sleep(1)
pyautogui.doubleClick(437, 222)
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('esc') 