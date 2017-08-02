import config
from bin.podcast_collection import PodcastCollection
import os 

def get_podcast_collection(podcast_name):
	podcast_location = config.PODCAST_DIRECTORY + os.sep + podcast_name
	collection = PodcastCollection(podcast_location)
	return collection

dick_collection = get_podcast_collection('files')