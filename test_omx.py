from omx import OMX
from time import sleep

video = "./data/video.mp4"
blank = "./data/logo.mp4"
omx = OMX()
omx.play(video,False)
loops = 25
while(loops >= 0):
   videoplay = "Video ended" if omx.playing() is False else "Video playing"
   print videoplay
   sleep(1)
   loops -= 1
