'''
Created on Jul 19, 2019

@author: Ethan
'''
from PIL import ImageGrab
import keyboard
import mouse

xBuffer = 1
xPos = [731, 882, 1034, 1185]
yStartPos = 30
yEndPos = 1040
colors = [(28, 82, 107), (11, 16, 28)]
#        Long tile        Short tile

#Wait until the key "j" is pressed to start
while not keyboard.is_pressed("j"):
    pass

print("Started")

while not keyboard.is_pressed("k"): #Fail safe
    screen = ImageGrab.grab() #Sample the screen
    for i in range(0, len(xPos), 1):
        for x in range(xPos[i] - xBuffer, xPos[i] + xBuffer, 1):
            for y in range(yEndPos, yStartPos, -1):
                color = screen.getpixel((x, y))
                if color in colors:
                    mouse.move(x, y)
                    mouse.click()
                    print("Found {0} at ({1}, {2})".format(color, x, y))