from omx import OMX

self.video = "./data/video.mp4"
self.blank = "./data/logo.mp4"
self.omx = OMX()
self.omx.play(self.video,False)
