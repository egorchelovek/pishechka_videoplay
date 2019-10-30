import sys, time, threading
from omxplayer.player import OMXPlayer
import RPi.GPIO as GPIO

class Pishechka():
    def run(self):
        self.init()

        thread_led = threading.Thread(target=self.blink)
        thread_led.start()

        thread_button = threading.Thread(target=self.check)
        thread_button.start()

        self.play(self.screensaver)
        while True:
            playing_video = self.video.is_playing()
            if not self.button_pushed_before and self.button_pushed_now:
                if self.screensaver.is_playing():
                    self.stop(self.screensaver)
                    self.play(self.video)
                else:
                    self.set_position(0)
            elif not playing_video:
                if not self.screensaver.is_playing():
                    self.play(self.screensaver)

            time.sleep(0.005)

        self.video.quit()
        self.screensaver.quit()
        thread_led.join()
        thread_button.join()

    def init(self):
        # init GPIO
        self.button_pin = 10
        self.led_pin = 8
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.button_pin,GPIO.IN)
        GPIO.setup(self.led_pin,GPIO.OUT)

        # init OMX
        screensaver_video = "/opt/pishechka_videoplay/data/screensaver.mp4"
        content_video = "/opt/pishechka_videoplay/data/content.mp4"
        self.screensaver = OMXPlayer(screensaver_video,args=['--no-osd','--loop'], dbus_name='org.mpris.MediaPlayer2.omxplayer1')
        self.stop(self.screensaver)
        self.video = OMXPlayer(content_video,args=['--no-osd'], dbus_name='org.mpris.MediaPlayer2.omxplayer2')
        self.stop(self.video)

    def stop(self,video):
        video.pause()
        video.hide_video()

    def play(self,video):
        video.show_video()
        video.play()

    def blink(self):
        while(True):
            GPIO.output(self.led_pin,True)
            time.sleep(0.5)
            GPIO.output(self.led_pin,False)
            time.sleep(0.5)

    def check(self):
        self.button_pushed_before = False
        self.button_pushed_now = False
        while(True):
            self.button_pushed_now = GPIO.input(self.button_pin)
            time.sleep(0.125)
            self.button_pushed_before = self.button_pushed_now


if __name__ == "__main__":
    pishechka = Pishechka()
    pishechka.run()
