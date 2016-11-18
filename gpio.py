import logging
from gpiozero import LED, Button
from RPi import GPIO
from time import sleep
import subprocess

log = logging.getLogger(__name__)
# 3.3v		5V
# gpio2		5V
# gpio3		GND
# gpio4		gpio14
# GND		gpio15
# gpio17	gpio18


#red = LED(17)	  # 6th pin (5th from top) on left
#button = Button(2) # second from top on left

def config():
    subprocess.call('./config_gpio.sh')

def get_pin():
    txt = subprocess.check_output(['gpio', 'read', '8'])
    return int(txt)

def set_pin(high=True):
    subprocess.call(['gpio', 'write', '0', '1' if high else '0'])

while False: #True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)

    if button.is_pressed:
        print('Button is pressed')
    else:
        print('Button not pressed')
