from bin.io.json_config import JsonConfig
import os

# used to see if a file has been played
# by this application. if the file is in 
# the .podcast.json file, it is assumed,
# that the episode has been played
class PodcastDirectoryConfig: 
	def __init__(self, directory):
		full_directory_path = os.path.abspath(os.path.dirname(directory))
		file_name = ".podcast.json"
		self.engine = JsonConfig(full_directory_path + os.sep + file_name)
		self.config = self.engine.config

		# make sure we have all sections in the 
		# config defined that we need. 
		self.config['episodes'] = self.config.get('episodes', [])

	def episode__played(self, name):
		if self.is_episode_played(name) == False:
			self.config['episodes'].append(name)

	def is_episode_played(self, name):
		for song in self.config['episodes']:
			if song == name: 
				# we found the song, it's been played
				return True

		return False

	def save(self):
		self.engine.config = self.config 
		self.engine.save()