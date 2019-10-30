import RPi.GPIO as GPIO
import time   

# init GPIO
led_pin = 8
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT)
count = 5
while count >= 0:
    GPIO.output(led_pin,True)
    time.sleep(0.5)
    GPIO.output(led_pin,False)
    time.sleep(0.5)
    count -= 1
