from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

def altTab():
    pyautogui.keyDown('alt')
    time.sleep(.1)
    pyautogui.press('tab')
    time.sleep(.1)
    pyautogui.keyUp('alt')

altTab()

while keyboard.is_pressed('q') == False:
    click(953,542)

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
