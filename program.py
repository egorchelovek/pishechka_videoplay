import sys, time, threading
from omxplayer.player import OMXPlayer
import RPi.GPIO as GPIO

class Pishechka():
    def run(self):
        self.init()

        # lights up led
        GPIO.output(self.led_pin,True)

        # run screensaver video
        self.play(self.screensaver)

        button_pushed_before = False
        button_pushed_now = False
        while True:
            # poll button
            button_pushed_now = GPIO.input(self.button_pin)

            # react only for changing button state from LOW to HIGH
            if not button_pushed_before and button_pushed_now:
                # button pushed
                if self.screensaver.is_playing():
                    self.stop(self.screensaver)
                    self.play(self.video)
                else:
                    # start video from the begining
                    self.video.set_position(0)

            # waiting and save button old state
            time.sleep(0.125)
            button_pushed_before = button_pushed_now

        self.video.quit()
        self.screensaver.quit()

    def init(self):
        # init GPIO
        GPIO.setmode(GPIO.BOARD)
        # set up pins
        self.button_pin = 10
        self.led_pin = 8
        #
        GPIO.setup(self.button_pin,GPIO.IN)
        GPIO.setup(self.led_pin,GPIO.OUT)

        # init OMX players
        screensaver_video = "/opt/pishechka_videoplay/data/screensaver.mp4"
        content_video = "/opt/pishechka_videoplay/data/content.mp4"
        #
        self.screensaver = OMXPlayer(screensaver_video,args=['--no-osd','--loop'], dbus_name='org.mpris.MediaPlayer2.omxplayer1')
        self.stop(self.screensaver)
        #
        self.video = OMXPlayer(content_video,args=['--no-osd','--loop'], dbus_name='org.mpris.MediaPlayer2.omxplayer2')
        self.stop(self.video)

    def stop(self,video):
        video.pause()
        video.hide_video()

    def play(self,video):
        video.show_video()
        video.play()


if __name__ == "__main__":
    pishechka = Pishechka()
    pishechka.run()
