#!/usr/bin/python3

import sys, time, threading
from daemon import Daemon

import RPi.GPIO as GPIO
from omm import OMM

class MyDaemon(Daemon):
        def run(self):
		        self.init()
                threading.Thread(target=self.blink()).start()
                button_push_old = False
                self.omm.play(self.blank,True)
                while True:
                    button_push_now = GPIO.input(button_pin)
                    if button_push_old != button_push_now and button_push_now = True:
                        self.omm.stop()
                        self.omm.play(self.video)
                    else if self.omm.p.poll() is None:
                        omm.play(self.blank,True)
                    button_push_old = button_push_now
                    time.sleep(0.125)

        def init(self):
            # init GPIO
            self.button_pin = 8
            self.led_pin = 12
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(button_pin,GPIO.IN)
            GPIO.setup(led_pin,GPIO.OUT)

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
        daemon = MyDaemon('/tmp/daemon-example.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)
