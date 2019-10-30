#!/usr/bin/python3

from subprocess import Popen, PIPE
from time import sleep
import sys, select, os
import requests

class OMX:
    def play(self, ifile, loop):
        #print("play : {}".format(infile))

        if "http" in ifile:
            try:
                r = requests.head(infile)
                #print(r.status_code)
            except requests.ConnectionError:
                return("{} :- failed to connect".format(infile))
        elif not os.path.exists(ifile):
            return "File {} not Found".format(ifile)

        try:
            if loop == True:
                self.p = Popen(["/usr/bin/omxplayer", "--no-osd", "--loop", ifile],
                 stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True,
                     bufsize=0, close_fds=True)
            else:
                self.p = Popen(["/usr/bin/omxplayer", "--no-osd", ifile],
                 stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True,
                     bufsize=0, close_fds=True)
        except:
            out, err = self.p.communicate()
            out = out.decode("utf-8").rstrip("\n")
            return out
        return

    def pause(self):
        self.p.stdin.write("p")
        return

    def stop(self):
        self.p.stdin.write("q")
        sleep(1)
        return

    def speed(self, updwn):
        if updwn == "up":
            self.p.stdin.write("2")
        else:
            self.p.stdin.write("1")
        return

    def vol(self, updwn):
        if updwn == "up":
            self.p.stdin.write("+")
        else:
            self.p.stdin.write("-")
        return

    def state(self):
        return self.p.poll()
