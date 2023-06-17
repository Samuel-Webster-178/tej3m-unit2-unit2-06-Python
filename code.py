# Created by: Samuel Webster
# Created on: June 2023
#
#  Uses a HC-SR04 Ultrasonic sensor to check the distance.

import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP21, echo_pin=board.GP20)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("error")
    time.sleep(0.1)
