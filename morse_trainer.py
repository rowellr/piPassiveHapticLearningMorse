##################################################
# This is part of PiPHL the RaspberryPi Passive
# Haptic Learning tool
#
# Copyright 2017 Paul Warren <pwarren@pwarren.id.au>
#
# Released under the GNU Public License Version 3.0 or later.
##################################################

import time
from Adafruit_DRV2605 import *

drv = Adafruit_DRV2605(busnum=0)

### setup ###
drv.begin()

# I2C trigger by sending 'go' command
drv.setMode(DRV2605_MODE_INTTRIG)  # default, internal trigger when sending GO command
drv.selectLibrary(1)

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
        time.sleep(0.33)


def a():
        dit(); dah();
        wait_letter()

def b():
        dah(); dit(); dit(); dit();
        wait_letter()

def c():
        dah(); dit(); dah(); dit()
        wait_letter()

def d():
        dah(); dit(); dit();
        wait_letter()

def e():
        dit();
        wait_letter()

def f():
        dit(); dit(); dah(); dit();
        wait_letter()

def g():
        dah(); dah(); dit();
        wait_letter()

def h():
        dit(); dit(); dit(); dit();
        wait_letter()

def i():
        dit(); dit();
        wait_letter()

def j():
        dit(); dah(); dah(); dah();
        wait_letter()

def k():
        dah(); dit(); dah();
        wait_letter()
        
def l():
        dit(); dah(); dit(); dit();
        wait_letter()
        
def m():
        dah(); dah();
        wait_letter()
        
def n():
        dah(); dit();
        wait_letter()

def O():
        dah(); dah(); dah();
        wait_letter()

def p():
        dit(); dah(); dah(); dit();
        wait_letter()

def q():
        dah(); dah(); dit(); dah();
        wait_letter()

def r():
        dit(); dah(); dit();
        wait_letter()
        
def s():
        dit(); dit(); dit();
        wait_letter()
        
def t():
        dah();
        wait_letter()
        
def u():
        dit(); dit(); dah();
        wait_letter()
        
def v():
        dit(); dit(); dit(); dah();
        wait_letter()
        
def w():
        dit(); dah(); dah();
        wait_letter()
        
def x():
        dah(); dit(); dit(); dah();
        wait_letter()
        
def y():
        dah(); dit(); dah(); dah();
        wait_letter()
        
def z():
        dah(); dah(); dit(); dit();
        wait_letter()
        
def m1():
        dit(); dah(); dah(); dah(); dah();
        wait_letter()
        
def m2():
        dit(); dit(); dah(); dah(); dah();
        wait_letter()
        
def m3():
        dit(); dit(); dit(); dah(); dah();
        wait_letter()
        
def m4():
        dit(); dit(); dit(); dit(); dah();
        wait_letter()
        
def m5():
        dit(); dit(); dit(); dit(); dit();
        wait_letter()
        
def m6():
        dah(); dit(); dit(); dit(); dit();
        wait_letter()
        
def m7():
        dah(); dah(); dit(); dit(); dit();
        wait_letter()
        
def m8():
        dah(); dah(); dah(); dit(); dit();
        wait_letter()
                
def m9():
        dah(); dah(); dah(); dah(); dit();
        wait_letter()
        
def m0():
        dah(); dah(); dah(); dah(); dah();
        wait_letter()


print "A"
a()
print "B"
b()


print "C"
c()
print "Q"
q()


print "V"
v()
print "K"
k()
print "1"
m1()
print "A"
a()
print "T"
t()
print "P"
p()
