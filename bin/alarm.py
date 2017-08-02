import os
import schedule

from Tkinter import *

from pygame import mixer

print('Loading Alarm Module')
class Alarm: 

	# Create an alarm that will sound. 
	# Params 
	# 	weekday : day of the week to play the alarm, ex. 0 for sunday
	#	hour : military time hour that you want the alarm to be scheduled for
	# 	minute: the minute of the hour that 
	def __init__(self, weekday, at, directory):
		self.directory = directory 
		self.print_feedback(weekday, at, directory)
		
		if weekday == 'sunday': 
			schedule.every().sunday.at(at).do(self.play_podcast)
		elif weekday == 'monday': 
			schedule.every().monday.at(at).do(self.play_podcast)
		elif weekday == 'tuesday': 
			schedule.every().tuesday.at(at).do(self.play_podcast)
		elif weekday == 'wednesday': 
			schedule.every().wednesday.at(at).do(self.play_podcast)
		elif weekday == 'thursday': 
			schedule.every().thursday.at(at).do(self.play_podcast)
		elif weekday == 'friday': 
			schedule.every().friday.at(at).do(self.play_podcast)
		elif weekday == 'saturday': 
			schedule.every().saturday.at(at).do(self.play_podcast)

	def play_podcast(self):
		print("Playing podcast")
		root = Tk()

		mixer.init()
		mixer.music.load('files/podcast.mp3')
		mixer.music.play()

		root.mainloop()

	def print_feedback(self, weekday, at, directory):
		print("Setting alarm for '" + weekday + "' at '" + at + "' to play podcast from '" + directory + "'")
