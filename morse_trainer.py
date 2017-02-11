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
from morse import Morse

from Adafruit_DRV2605 import *
	

def generateSequence(size, chars=string.ascii_lowercase + string.digits):
	retval = []
	for i in range(size):
		retval.append(random.choice(chars))
	return retval

def main():
	drv = Adafruit_DRV2605(busnum=0)
	drv.begin()
	drv.setMode(DRV2605_MODE_INTTRIG)  
	drv.selectLibrary(1)

	morse_player = Morse(drv)
	
	while(1):
		sequence = generateSequence(64) 
		for item in sequence:
			print item
			morse_player.play_letter(item)
			time.sleep(0.5)

if __name__ == '__main__':
	main()
				
