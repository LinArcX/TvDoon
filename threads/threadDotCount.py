import sys
import time
import threading

from utility import constants

class threadDotCount(threading.Thread):
    def __init__(self, threadID, name, daemon):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.daemon = daemon
    def run(self):
        dotCountRun()

def dotCountRun():
    infoCounter = 0
    while constants.wholeCounter:
        if infoCounter == 0:
            sys.stdout.write("\r%s" % '')
            sys.stdout.flush()
            infoCounter = 1
            time.sleep(0.1)
        elif infoCounter == 1:
            sys.stdout.write("\r%s" % '.')
            sys.stdout.flush()
            infoCounter = 2
            time.sleep(0.1)
        elif infoCounter == 2:
            sys.stdout.write("\r%s" % '..')
            sys.stdout.flush()
            infoCounter = 3
            time.sleep(0.1)
        elif infoCounter== 3:
            sys.stdout.write("\r%s" % '...')
            sys.stdout.flush()
            infoCounter = 0
            time.sleep(0.1)