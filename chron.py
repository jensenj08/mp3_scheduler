import schedule
import time
from bin.alarm import Alarm
import config

print(config.test)

alarm1 = Alarm('tuesday','22:27', 'folder')

while 1:
    schedule.run_pending()
    time.sleep(1)