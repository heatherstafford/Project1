#Heather Stafford
#4/4/18
#bullsAndCows.py - Project #1

from ggame import *
from random import randint

RADIUS = 22

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

def green(Event):
    Sprite(CircleAsset(RADIUS, LineStyle(2,Color(0x006600,1)), colg))
    
def red(Event):
    Sprite(CircleAsset(RADIUS,LineStyle(2,Color(0xFF0000,1)), colr))

def yellow(Event):
    Sprite(CircleAsset(RADIUS,LineStyle(2,Color(0xFFFF00,1)),coly))
    
def purple(Event):
    Sprite(CircleAsset(RADIUS,LineStyle(2,Color(0xc300ff,1)), colp))
    
def blue(Event):
    Sprite(CircleAsset(RADIUS,LineStyle(2,Color(0x003bff,1)), colb))
    
    
circle = CircleAsset(RADIUS, LineStyle(2,Color(0x000000,1)),Color(0xFFFFFF,1))
    
for i in range(4):
    for j in range(10):
        Sprite(circle,(10 + (2*RADIUS+10)*i,10 + (2*RADIUS+10)*j)) #putting a row of dots

App().listenKeyEvent('keydown','g',green)
App().listenKeyEvent('keydown','r', red)
App().listenKeyEvent('keydown','y', yellow)
App().listenKeyEvent('keydown','p', purple)
App().listenKeyEvent('keydown','b', blue)

App().run()