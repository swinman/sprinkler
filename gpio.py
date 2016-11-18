from gpiozero import LED, Button
from time import sleep

# 3.3v		5V
# gpio2		5V
# gpio3		GND
# gpio4		gpio14
# GND		gpio15
# gpio17	gpio18


red = LED(17)	  # 6th pin (5th from top) on left
button = Button(2) # second from top on left


while False: #True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)

    if button.is_pressed:
        print('Button is pressed')
    else:
        print('Button not pressed')
