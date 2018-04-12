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
    while data['rows'] < 10:
        data['guess1'] = 'Green'
        break
    while data['rows'] < 60:
        data['guess2'] = 'Green'
        break
    while data['rows'] < 110:
        data['guess3'] = 'Green'
        break
    while data['rows'] < 130:
        data['guess4'] = 'Green'
        break
    while data['rows'] < 120:
        data['rows'] += 50
        break
    
#circle changes to red
def red(Event):
    redCircle = (CircleAsset(RADIUS,LineStyle(2,Color(0x000000,1)), Color(0xFF0000,1)))
    Sprite(redCircle,(data['rows'], data['cols']))
    while data['rows'] < 10:
        data['guess1'] = 'Red'
        break
    while data['rows'] < 60:
        data['guess2'] = 'Red'
        break
    while data['rows'] < 110:
        data['guess3'] = 'Red'
        break
    while data['rows'] < 130:
        data['guess4'] = 'Red'
        break
    while data['rows'] < 120:
        data['rows'] += 50
        break
    
#circle changes to yellow
def yellow(Event):
    yellowCircle = (CircleAsset(RADIUS,LineStyle(2,Color(0x000000,1)),Color(0xFFFF00,1)))
    Sprite(yellowCircle,(data['rows'], data['cols']))
    while data['rows'] < 10:
        data['guess1'] = 'Yellow'
        break
    while data['rows'] < 60:
        data['guess2'] = 'Yellow'
        break
    while data['rows'] < 110:
        data['guess3'] = 'Yellow'
        break
    while data['rows'] < 130:
        data['guess4'] = 'Yellow'
        break
    while data['rows'] < 120:
        data['rows'] += 50
        break
    
#circle changes to purple
def purple(Event):
    purpleCircle = (CircleAsset(RADIUS,LineStyle(2,Color(0x000000,1)), Color(0xc300ff,1)))
    Sprite(purpleCircle,(data['rows'], data['cols']))
    while data['rows'] < 10:
        data['guess1'] = 'Purple'
        break
    while data['rows'] < 60:
        data['guess2'] = 'Purple'
        break
    while data['rows'] < 110:
        data['guess3'] = 'Purple'
        break
    while data['rows'] < 130:
        data['guess4'] = 'Purple'
        break
    while data['rows'] < 120:
        data['rows'] += 50
        break
 
#circle changes to blue   
def blue(Event):
    blueCircle = (CircleAsset(RADIUS,LineStyle(2,Color(0x000000,1)), Color(0x003bff,1)))
    Sprite(blueCircle,(data['rows'], data['cols']))
    while data['rows'] < 10:
        data['guess1'] = 'Blue'
        break
    while data['rows'] < 60:
        data['guess2'] = 'Blue'
        break
    while data['rows'] < 110:
        data['guess3'] = 'Blue'
        break
    while data['rows'] < 130:
        data['guess4'] = 'Blue'
        break
    while data['rows'] < 120:
        data['rows'] += 50
        break

#Makes the computer check the codes and move where the person is entering the color when enter is pressed
def enter(Event):
    checkCode1()
    checkCode2()
    checkCode3()
    checkCode4()
    data['cols'] += 50
    data['rows'] -= 150
    updateScore()
    
#Checks the entered 1st color with the computers code
def checkCode1():
    if data['code1'] == data['guess1']:
        data['bulls'] += 1
    elif data['code1'] == data['guess2']:
        data['cows'] += 1
    elif data['code1'] == data['guess3']:
        data['cows'] += 1
    elif data['code1'] == data['guess4']:
        data['cows'] += 1
    else:
        data['bulls'] += 0
        
#Checks the entered 2nd color with the computers code
def checkCode2():
    if data['code2'] == data['guess2']:
        data['bulls'] += 1
    elif data['code2'] == data['guess1']:
        data['cows'] += 1
    elif data['code2'] == data['guess3']:
        data['cows'] += 1
    elif data['code2'] == data['guess4']:
        data['cows'] += 1
    else:
        data['bulls'] += 0

#Checks the entered 3rd color with the computers code
def checkCode3():
    if data['code3'] == data['guess3']:
        data['bulls'] += 1
    elif data['code3'] == data['guess1']:
        data['cows'] += 1
    elif data['code3'] == data['guess2']:
        data['cows'] += 1
    elif data['code3'] == data['guess4']:
        data['cows'] += 1
    else:
        data['bulls'] += 0

#Checks the entered 4th color with the computers code
def checkCode4():
    if data['code4'] == data['guess4']:
        data['bulls'] += 1
    elif data['code4'] == data['guess1']:
        data['cows'] += 1
    elif data['code4'] == data['guess2']:
        data['cows'] += 1
    elif data['code4'] == data['guess3']:
        data['cows'] += 1
    else:
        data['bulls'] += 0

#makes the score appear on the screen
def updateScore():
    data['bullscore'].destroy() 
    data['cowscore'].destroy() 
    bullScore = TextAsset('Bulls = ' + str(data['bulls']))
    cowScore = TextAsset('Cows = ' + str(data['cows']))
    data['bullscore'] = Sprite(bullScore, (200,200))
    data['cowscore'] = Sprite(cowScore, (200,150))


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
    data['guess1'] = ''
    data['guess2'] = ''
    data['guess3'] = ''
    data['guess4'] = ''

    circle = CircleAsset(RADIUS, LineStyle(2,Color(0x000000,1)),Color(0xFFFFFF,1))
    bullScore = TextAsset('Bulls = ' + str(data['bulls']))
    cowScore = TextAsset('Cows = ' + str(data['cows']))
    data['bullscore'] = Sprite(bullScore, (200,200))
    data['cowscore'] = Sprite(cowScore, (200,150))
    
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
    