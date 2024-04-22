import pyautogui as py
import time as t
import keyboard as keyboard
t.sleep(0.5)

# 400,260    1560,260

# 400,825    1560,825

# rgb(149,195,232)
#(149, 195, 232)
#blue (43,134,208)

# print(py.pixel(400,260))
py.click(952,521)
while keyboard.is_pressed('s') == False:
    pic = py.screenshot(region=(400,260,1160,565))
    width,height = pic.size
    for x in range (0,width,60):
        for y in range(0,height,60):
            r,g,b = pic.getpixel((x,y))
            if r in range(145,155) or g in range(190,200):
                py.click(x+400,y+260)
                # print(x+400,y+260)
                # t.sleep(0.07)
                break
            # else:
            #     py.click(973,740)
