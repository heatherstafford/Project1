#Heather Stafford
#4/4/18
#bullsAndCows.py - Project #1

from ggame import *
from random import randint

RADIUS = 10

def pickCode():
    randint(0,4)
    0 = Color(0x006600,1) #Green
    1 = Color(0xFF0000,1) #Red
    2 = Color(0xFFFF00,1) #yellow
    3 = Color(0xc300ff,1) #Purple
    4 = Color(0x003bff,1) #Blue
    

cicle = CircleAsset(