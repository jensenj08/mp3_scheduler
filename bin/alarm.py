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
	def __init__(self, weekday, at, action):
		self.print_feedback(weekday, at)
		
		if weekday == 'sunday': 
			schedule.every().sunday.at(at).do(action)
		elif weekday == 'monday': 
			schedule.every().monday.at(at).do(action)
		elif weekday == 'tuesday': 
			schedule.every().tuesday.at(at).do(action)
		elif weekday == 'wednesday': 
			schedule.every().wednesday.at(at).do(action)
		elif weekday == 'thursday': 
			schedule.every().thursday.at(at).do(action)
		elif weekday == 'friday': 
			schedule.every().friday.at(at).do(action)
		elif weekday == 'saturday': 
			schedule.every().saturday.at(at).do(action)

	def play_podcast(self):
		print("Playing podcast")
		root = Tk()

		mixer.init()
		mixer.music.load('files/podcast.mp3')
		mixer.music.play()

		root.mainloop()

	def print_feedback(self, weekday, at):
		print("Setting alarm for '" + weekday + "' at '" + at + "' to play podcast")
