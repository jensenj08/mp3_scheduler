#! python
import glob, os, time
from Tkinter import *
from pygame import mixer
from bin.io.json_config import PodcastDirectoryConfig


class PodcastCollection:
	# initialize. shows where the full path to the 
	# podcast files are and sets the oldest file in the 
	# directory to play next
	def __init__(self, podcast_path):
		print('Initializing Podcast Collection From ' + podcast_path)
		self.path = podcast_path
		self.config = PodcastDirectoryConfig(podcast_path)
		
	# get the oldest file from the directory and 
	# set it to play next
	def get_next_file(self):
		files = sorted(os.listdir(self.path), key=os.path.getmtime)
		self.current_file = self.path + os.sep + files[0]

		# check if the file has been played
		for file in files:
			if self.config.is_episode_played(file) == False:
				self.current_file = self.path + os.sep + file

		self.config.episode_played(file)
		self.config.save()
		
		print("Setting file to play: '" + self.current_file + "'")

	# play the current file
	def play(self):
		self.get_next_file()
		root = Tk()
		mixer.init()
		mixer.music.load(self.current_file)
		mixer.music.play()
		root.mainloop()
			