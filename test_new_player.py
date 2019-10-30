from omxplayer.player import OMXPlayer
from time import sleep

path = "./data/"
#playlist_file = open(path")
#movie = playlist_file.read().split("\n")

player0 = OMXPlayer(path+"video.mp4",args=['--no-osd'], dbus_name="org.mpris.MediaPlayer2.omxplayer1")
player0.pause()
player1 = OMXPlayer(path+"logo.mp4",args=['--no-osd'], dbus_name="org.mpris.MediaPlayer2.omxplayer2")
player1.pause()
player1.hide_video()

player0.play()
sleep(5)
player0.pause()
player0.hide_video()

player1.show_video()
player1.play()
sleep(3)

player0.quit()
player1.quit()
