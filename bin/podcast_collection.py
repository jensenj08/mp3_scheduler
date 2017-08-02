#! python
import glob, os
import time

class PodcastCollection:

		def __init__(self, podcast_path):
			print('Initializing Podcast Collection From ' + podcast_path)
			self.path = podcast_path
			
			# get directory 
			mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    		self.files = list(sorted(os.listdir(self.path), key=mtime))
			self.current_file = files[0]
			

			