import schedule, time, os
from bin.alarm import Alarm
from bin.podcast_collection import PodcastCollection
import config

podcast = PodcastCollection(config.PODCAST_DIRECTORY + os.sep + 'files')
alarm1 = Alarm('tuesday','23:31', podcast.play)

while 1:
    schedule.run_pending()
    time.sleep(1)