#Heather Stafford
#4/4/18
#bullsAndCows.py - Project #1

from ggame import *
from random import randint

RADIUS = 20
ROWS = 10
COLS = 10

#Computer randomly generates the colors for guessing
def pickCode():
    num = (randint(0,4), randint(0,4), randint(0,4), randint(0,4))
    if num == 0: 
        col = Color(0x006600,1) #Green
    elif num == 1:
        col = Color(0xFF0000,1) #Red
    elif num == 2:
        col = Color(0xFFFF00,1) #yellow
    elif num == 3:
        col = Color(0xc300ff,1) #Purple
    else:
        col = Color(0x003bff,1) #Blue
    
#circle changes to green
def green(Event):
    greenCircle = (CircleAsset(RADIUS, LineStyle(2,Color(0x000000,1)), Color(0x006600,1)))
    Sprite(greenCircle,(data['rows'], data['cols']))
    data['rows'] += 50
    
#circle changes to red
def red(Event):
    redCircle = (CircleAsset(RADIUS,LineStyle(2,Color(0x000000,1)), Color(0xFF0000,1)))
    Sprite(redCircle,(data['rows'], data['cols']))
    While data['rows'] < 120:
        data['rows'] += 50
    
#circle changes to yellow
def yellow(Event):
    yellowCircle = (CircleAsset(RADIUS,LineStyle(2,Color(0x000000,1)),Color(0xFFFF00,1)))
    Sprite(yellowCircle,(data['rows'], data['cols']))
    data['rows'] += 50
    
#circle changes to purple
def purple(Event):
    purpleCircle = (CircleAsset(RADIUS,LineStyle(2,Color(0x000000,1)), Color(0xc300ff,1)))
    Sprite(purpleCircle,(data['rows'], data['cols']))
    data['rows'] += 50
 
#circle changes to blue   
def blue(Event):
    blueCircle = (CircleAsset(RADIUS,LineStyle(2,Color(0x000000,1)), Color(0x003bff,1)))
    Sprite(blueCircle,(data['rows'], data['cols']))
    data['rows'] += 50
"""
def enter(Event):
    

#checks to see if the computers code is the same as the one entered
def checkCode():
    if 
"""
#sets up and runs the game
if __name__ == '__main__':  

    #hold variables in a dictionary
    data = {}
    data['rows'] = 10
    data['cols'] = 10

    circle = CircleAsset(RADIUS, LineStyle(2,Color(0x000000,1)),Color(0xFFFFFF,1))
    
    #Creates board of circles
    for i in range(4):
        for j in range(10):
            Sprite(circle,(10 + (2*RADIUS+10)*i,10 + (2*RADIUS+10)*j)) #putting a row of dots

    App().listenKeyEvent('keydown','g',green)
    App().listenKeyEvent('keydown','r', red)
    App().listenKeyEvent('keydown','y', yellow)
    App().listenKeyEvent('keydown','p', purple)
    App().listenKeyEvent('keydown','b', blue)
    """
    App().listenKeyEvent('keydown','enter', enter)
    """
    App().run()
    