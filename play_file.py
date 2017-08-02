#! python

from Tkinter import *
root = Tk()

from pygame import mixer
mixer.init()
mixer.music.load('files/podcast.mp3')
mixer.music.play()

root.mainloop()