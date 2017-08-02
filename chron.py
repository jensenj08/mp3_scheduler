import schedule, time, os
from bin.alarm import Alarm
from bin.podcast_collection import PodcastCollection
import json

def line(): 
	print('----------------------------------------------------------------------')

# read data from configuration file
with open('config.json') as json_data_file:
    data = json.load(json_data_file)

# set alarm for that time
line()
for podcast_config in data['podcasts'] : 
	podcast = PodcastCollection(podcast_config['path'])
	alarm1 = Alarm(podcast_config['weekday'], podcast_config['at'], podcast.play)
	line()

while 1:
    schedule.run_pending()
    time.sleep(1)