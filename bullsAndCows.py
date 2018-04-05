#Heather Stafford
#4/4/18
#bullsAndCows.py - Project #1

from ggame import *
from random import randint

RADIUS = 10

def pickCode():
    num = randint(0,4)
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

key=event.key

def enterColor(Event):
    if key = b:
    
circle = CircleAsset(RADIUS, LineStyle(2,col),col)
    
for i in range(20):
    for j in range(20):
        Sprite(circle,(10 + (2*RADIUS+10)*i,10 + (2*RADIUS+10)*j)) #putting a row of dots

App().run()