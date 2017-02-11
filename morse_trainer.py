##################################################
# This is part of PiPHL the RaspberryPi Passive
# Haptic Learning tool
#
# Copyright 2017 Paul Warren <pwarren@pwarren.id.au>
#
# Released under the GNU Public License Version 3.0 or later.
##################################################

import time
import string
import random

from Adafruit_DRV2605 import *

drv = Adafruit_DRV2605(busnum=0)

### setup ###
drv.begin()

# I2C trigger by sending 'go' command
drv.setMode(DRV2605_MODE_INTTRIG)  
drv.selectLibrary(1)


##################################################
# Dahs and Dits arrived at by trial and error
# Feel free to find one that works for you!
# see http://www.ti.com/lit/ds/symlink/drv2605.pdf for more info!
##################################################

def dah():
    drv.setWaveform(0, 14)
    drv.setWaveform(1, 0)  
    drv.go()
    time.sleep(0.32)
	
def dit():
    drv.setWaveform(0, 1)
    drv.setWaveform(1, 0)  
    drv.go()
    time.sleep(0.18)

def wait_letter():
    time.sleep(0.33)

def wait_word():
    time.sleep(0.45)

def a():
    dit(); dah();
    

def b():
    dah(); dit(); dit(); dit();
    

def c():
    dah(); dit(); dah(); dit()
    

def d():
    dah(); dit(); dit();
    

def e():
    dit();
    

def f():
    dit(); dit(); dah(); dit();
    

def g():
    dah(); dah(); dit();
    

def h():
    dit(); dit(); dit(); dit();
    

def i():
    dit(); dit();
    

def j():
    dit(); dah(); dah(); dah();
    

def k():
    dah(); dit(); dah();
    
        
def l():
    dit(); dah(); dit(); dit();
    
        
def m():
    dah(); dah();
    
        
def n():
    dah(); dit();
    

def O():
    dah(); dah(); dah();
    

def p():
    dit(); dah(); dah(); dit();
    

def q():
    dah(); dah(); dit(); dah();
    

def r():
    dit(); dah(); dit();
    
        
def s():
    dit(); dit(); dit();
    
        
def t():
    dah();
    
        
def u():
    dit(); dit(); dah();
    
        
def v():
    dit(); dit(); dit(); dah();
    
        
def w():
    dit(); dah(); dah();
    
        
def x():
    dah(); dit(); dit(); dah();
    
        
def y():
    dah(); dit(); dah(); dah();
    
        
def z():
    dah(); dah(); dit(); dit();
    
        
def m1():
    dit(); dah(); dah(); dah(); dah();
    
        
def m2():
    dit(); dit(); dah(); dah(); dah();
    
        
def m3():
    dit(); dit(); dit(); dah(); dah();
    
        
def m4():
    dit(); dit(); dit(); dit(); dah();
    
        
def m5():
    dit(); dit(); dit(); dit(); dit();
    
        
def m6():
    dah(); dit(); dit(); dit(); dit();
    
        
def m7():
    dah(); dah(); dit(); dit(); dit();
    
        
def m8():
    dah(); dah(); dah(); dit(); dit();
    
                
def m9():
    dah(); dah(); dah(); dah(); dit();
    
        
def m0():
    dah(); dah(); dah(); dah(); dah();
    


def play_morse(alphanum):
	gettatr(self, alphanum)()
	wait_letter()


def generateSequence(size, chars=string.ascii_lowercase + string.digits):
	return random.sample(chars, size)

def main(args, kwargs):
		
    while(1):
        
        # generate sequence
		
        sequence = generateSequence(64) 
        
        # play sequence!
        for item in sequence:
            print item

			
			

