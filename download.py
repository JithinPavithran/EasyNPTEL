from Queue import Queue
from time import sleep

from PyQt4.QtCore import QThread
import urllib


class DownloadFile(object):
    def __init__(self, url, file_name, index, update_progress):
        self.url = url
        self.fileName = file_name
        self.index = index
        self.updateProgress = update_progress


class DownloadQueue(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.downloadQueue = Queue()

    def run(self):
        downloader = urllib.URLopener()
        downloader.addheaders = [('User-Agent',
                                  'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')]
        while True:
            while not self.downloadQueue.empty():
                print "Download Queue not empty"
                file = self.downloadQueue.get()
                print "downloading from ", file.url
                downloader.retrieve(file.url, file.fileName, file.updateProgress)

    def stopThread(self):
        self.terminate()

    def addToQueue(self, file):
        if self.dupExistFor(file):
            return
        self.downloadQueue.put(file)
        print file.fileName + " File added to queue(addToQueue)"
        if not self.isRunning():
            self.start()

    def dupExistFor(self, file):
        return False
        # TODO: Check for dups
        # for i in self.downloadQueue:
        #     if file == i:
        #         return True
        # return False
