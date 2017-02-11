# PiPHL
Haptic Passive Learning of Morse for the Raspberry Pi


# Objectives

This project aims to assist with learning morse code via a raspberryPi with a haptic motor and some headphones. Using techniques from the Haptic Passive Learning experiments run by the Georgia Institue of Technology.  [Their Paper](http://dl.acm.org/citation.cfm?id=2971768)


# TODO

- [X] talk to motor controller
- [X] record/find audio
- [X] document hardware choices
- [X] python library for motor controller
- [ ] python async audio playing
- [ ] generate sequences on the fly

# Hardware

 * RaspberryPi
 * [Adafruit DRV2605L Haptic Motor Controller](https://littlebirdelectronics.com.au/products/adafruit-drv2605l-haptic-motor-controller)
 * [Adafruit Vibrating Mini Motor Disc](https://littlebirdelectronics.com.au/products/vibrating-mini-motor-disc)

Links are to my local(ish) retailer of Adafruit goodness.

# Credits

 * Audio from: https://evolution.voxeo.com/tools/ under LGPL license.
 * DRV2605 python code from: https://github.com/spmealin/pyAdafruit_DRV2605 with changes by me to support the new adafruit_gpio Python packages.
