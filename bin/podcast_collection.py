#! python
import glob, os, time
from Tkinter import *
from pygame import mixer


class PodcastCollection:
	# initialize. shows where the full path to the 
	# podcast files are and sets the oldest file in the 
	# directory to play next
	def __init__(self, podcast_path):
		print('Initializing Podcast Collection From ' + podcast_path)
		self.path = podcast_path
		self.get_next_file()
		
	# get the oldest file from the directory and 
	# set it to play next
	def get_next_file(self):
		os.chdir(self.path)
		files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
		self.current_file = self.path + os.sep + files[0]
		print("Setting file to play: '" + self.current_file + "'")
		
	# play the current file
	def play(self):
		root = Tk()
		mixer.init()
		mixer.music.load(self.current_file)
		mixer.music.play()
		root.mainloop()
			