import sys, time, threading
from omm import OMM

class MyDaemon():
        def run(self):
		        self.init()
                threading.Thread(target=self.blink()).start()
                self.omm.play(self.video)
                while True:
                    if self.omm.p.poll() is None:
                        self.omm.play(self.blank,True)
                    time.sleep(0.125)

        def init(self):
            # init GPIO
            self.button_pin = 8
            self.led_pin = 12
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.button_pin,GPIO.IN)
            GPIO.setup(self.led_pin,GPIO.OUT)

            # init OMX
            self.video = "/path/to/video.mp4"
            self.blank = "/path/to/blank/video.mp4"
            self.omm = OMM()


        def blink(self):
            GPIO.output(self.led_pin,True)
            time.sleep(0.5)
            GPIO.ouput(self.led_pin,False)
            time.sleep(0.5)


if __name__ == "__main__":
    test = MyDaemon()
    test.run()
