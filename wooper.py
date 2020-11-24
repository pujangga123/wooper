import pyautogui as py
import time
import win32gui

# refs:
#   https://pyautogui.readthedocs.io/en/latest/quickstart.html#general-functions

# set active app
# py.hotkey('alt','tab')
hwnd = win32gui.FindWindow(None, "WhatsApp")
win32gui.SetForegroundWindow(hwnd)

# begin looping
for i in range(0,10):
    py.hotkey('ctrl','v')
    time.sleep(1)
    py.hotkey('ctrl','shift',']')
    time.sleep(1)

