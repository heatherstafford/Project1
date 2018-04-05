#Heather Stafford
#4/4/18
#bullsAndCows.py - Project #1

from ggame import *
from random import randint

RADIUS = 22

def pickCode():
    num = randint(0,4)
    if num == 0: 
        colg = Color(0x006600,1) #Green
    elif num == 1:
        colr = Color(0xFF0000,1) #Red
    elif num == 2:
        coly = Color(0xFFFF00,1) #yellow
    elif num == 3:
        colp = Color(0xc300ff,1) #Purple
    else:
        colb = Color(0x003bff,1) #Blue

def green(Event):
    CirlceAsset(RADIUS,LineStyle(2,Color(0x000000,1), colg)
    
def red(Event):
    CirlceAsset(RADIUS,LineStyle(2,Color(0x000000,1), colr)

def yellow(Event):
    CirlceAsset(RADIUS,LineStyle(2,Color(0x000000,1),coly)
    
def purple(Event):
    CirlceAsset(RADIUS,LineStyle(2,Color(0x000000,1), colp)
    
def blue(Event):
    CirlceAsset(RADIUS,LineStyle(2,Color(0x000000,1), colb)
    
    
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