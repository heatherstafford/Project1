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
    num1 = randint(0,4)
    if num1 == 0: 
        data['code1'] = 'Green' #Green
    elif num1 == 1:
        data['code1'] = 'Red' #Red
    elif num1 == 2:
        data['code1'] = 'Yellow' #yellow
    elif num1 == 3:
        data['code1'] = 'Purple' #Purple
    else:
        data['code1'] = 'Blue' #Blue
    
    num2 = randint(0,4)
    if num2 == 0: 
        data['code2'] = 'Green' #Green
    elif num2 == 1:
        data['code2'] = 'Red' #Red
    elif num2 == 2:
        data['code2'] = 'Yellow' #yellow
    elif num2 == 3:
        data['code2'] = 'Purple' #Purple
    else:
        data['code2'] = 'Blue' #Blue
        
    num3 = randint(0,4)
    if num3 == 0: 
        data['code3'] = 'Green' #Green
    elif num3 == 1:
        data['code3'] = 'Red' #Red
    elif num3 == 2:
        data['code3'] = 'Yellow' #yellow
    elif num3 == 3:
        data['code3'] = 'Purple' #Purple
    else:
        data['code3'] = 'Blue' #Blue
        
    num4 = randint(0,4)
    if num4 == 0: 
        data['code4'] = 'Green' #Green
    elif num4 == 1:
        data['code4'] = 'Red' #Red
    elif num4 == 2:
        data['code4'] = 'Yellow' #yellow
    elif num4 == 3:
        data['code4'] = 'Purple' #Purple
    else:
        data['code4'] = 'Blue' #Blue
    
#circle changes to green
def green(Event):
    greenCircle = (CircleAsset(RADIUS, LineStyle(2,Color(0x000000,1)), Color(0x006600,1)))
    Sprite(greenCircle,(data['rows'], data['cols']))
    while data['rows'] < 120:
        data['rows'] += 50
        break
    
#circle changes to red
def red(Event):
    redCircle = (CircleAsset(RADIUS,LineStyle(2,Color(0x000000,1)), Color(0xFF0000,1)))
    Sprite(redCircle,(data['rows'], data['cols']))
    while data['rows'] < 120:
        data['rows'] += 50
        break
    
#circle changes to yellow
def yellow(Event):
    yellowCircle = (CircleAsset(RADIUS,LineStyle(2,Color(0x000000,1)),Color(0xFFFF00,1)))
    Sprite(yellowCircle,(data['rows'], data['cols']))
    while data['rows'] < 120:
        data['rows'] += 50
        break
    
#circle changes to purple
def purple(Event):
    purpleCircle = (CircleAsset(RADIUS,LineStyle(2,Color(0x000000,1)), Color(0xc300ff,1)))
    Sprite(purpleCircle,(data['rows'], data['cols']))
    while data['rows'] < 120:
        data['rows'] += 50
        break
 
#circle changes to blue   
def blue(Event):
    blueCircle = (CircleAsset(RADIUS,LineStyle(2,Color(0x000000,1)), Color(0x003bff,1)))
    Sprite(blueCircle,(data['rows'], data['cols']))
    while data['rows'] < 120:
        data['rows'] += 50
        break

def enter(Event):
    checkCode()
    
#checks to see if the computers code is the same as the one entered
def checkCode():
    

#sets up and runs the game
if __name__ == '__main__':  

    #hold variables in a dictionary
    data = {}
    data['rows'] = 10
    data['cols'] = 10
    data['code1'] = ''
    data['code2'] = ''
    data['code3'] = ''
    data['code4'] = ''
    data['cows'] = 0
    data['bulls'] = 0

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
    App().listenKeyEvent('keydown','enter', enter)

    App().run()
    