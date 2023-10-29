import pyautogui as py
import time as t
import keyboard as keyboard

# the pixel you want to click: 1610 777
#blue: (43, 135, 209)
#green (75, 219, 106)

while keyboard.is_pressed('s') == False:
    if py.pixel(1610, 777) == (43,135,209) or py.pixel(1610, 777)==(75,219,106):
        tup = (1610,777)
        py.click(tup[0],tup[1])
