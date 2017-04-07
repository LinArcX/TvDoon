import threading
import pytvmaze
import sys

from datetime import datetime
from datetime import timedelta
from utility import constants

class threadSchedule(threading.Thread):
    def __init__(self, threadID, name, queue, currentDay, daemon, country='US', exceptdate=datetime.now().date()):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.queue = queue
        self.currentDay = currentDay
        self.daemon = daemon
        self.country = country
        self.exceptdate = exceptdate

    def run(self):
        scheduleRun(self.queue, self.currentDay, self.country, self.exceptdate)

def scheduleRun(queue, currentDay, country, exceptDay):
    itemDict = []
    deltaDays = (exceptDay - currentDay).days
    print("==== From: " + str(currentDay) + ", To: " + str(exceptDay) + " ====")
    for day in range(0, deltaDays+1):
        nextDay = currentDay + timedelta(days=day)
        url = pytvmaze.endpoints.get_schedule.format(country, nextDay)
        try:
            constants.wholeCounter = 1
            q = pytvmaze.TVMaze._endpoint_standard_get(url)
            constants.wholeCounter = 0

            # flush current characters from current line in terminal
            sys.stdout.write("\r%s" % '')
            sys.stdout.flush()


            print(str(day) + ": In: " + "'" + str(nextDay) + "'" + ", We Found:" + "'" + str(len(q)) + "'" + " Episodes.")
            itemDict.append([pytvmaze.Episode(episode) for episode in q]) #  [nextDay] = [pytvmaze.Episode(episode) for episode in q]
        except:
            print("In: " + "'" + str(nextDay) + "'" + ", We Found:" + "'0'" + " Episodes.")
    queue.put(itemDict)
    return
