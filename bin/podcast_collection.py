#! python
import glob, os, time
from Tkinter import *
from pygame import mixer
import io, json

class PodcastCollection:
	# initialize. shows where the full path to the 
	# podcast files are and sets the oldest file in the 
	# directory to play next
	def __init__(self, podcast_path):
		print('Initializing Podcast Collection From ' + podcast_path)
		self.path = podcast_path
		
	# get the oldest file from the directory and 
	# set it to play next
	def get_next_file(self):
		# get all files in the podcast directory 
		podcast_files = os.listdir(self.path)
		# get all files that have been played
		with open('config.json') as data_file:
			data = json.load(data_file)
			played_files = data['played']
			
		# find a file in the collection that hasn't been played
		for file in podcast_files: 
			if self.has_been_played(file, played_files) == False: 
				self.current_file = self.get_full_path(file)
				# update configuration file to include the file
				data['played'].append(self.current_file)
				with open('config.json', 'w') as outfile:
					json.dump(data, outfile)
	
	def get_full_path(self, file): 
		return self.path + os.sep + file 

	# check if the file has been played
	def has_been_played(self, file, played_files): 
		for played_file in played_files: 
			has_been_played = played_file == self.get_full_path(file)
			if has_been_played : 
				return True
			
		return False
	
	# play the current file
	def play(self):
		self.get_next_file()
		root = Tk()
		mixer.init()
		# this will cause an error...
		# instead, call get_next_file to be played inside of the play function itself
		mixer.music.load(self.current_file)
		mixer.music.play()
		root.mainloop()
			