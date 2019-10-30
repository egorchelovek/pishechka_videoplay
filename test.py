import sys, time, threading
from omx import OMX
import RPi.GPIO as GPIO

class MyDaemon():
        def run(self):
		self.init()
                threading.Thread(target=self.blink()).start()
                self.omx.play(self.video,False)
                while True:
                    if self.omx.state() is None:
                        self.omx.play(self.blank,True)
                    time.sleep(0.125)

        def init(self):
            # init GPIO
            self.button_pin = 8
            self.led_pin = 12
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.button_pin,GPIO.IN)
            GPIO.setup(self.led_pin,GPIO.OUT)

            # init OMX
            self.video = "./data/video.mp4"
            self.blank = "./data/logo.mp4"
            self.omx = OMX()


        def blink(self):
            GPIO.output(self.led_pin,True)
            time.sleep(0.5)
            GPIO.output(self.led_pin,False)
            time.sleep(0.5)


if __name__ == "__main__":
    test = MyDaemon()
    test.run()
