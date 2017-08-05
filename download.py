from PyQt4.QtCore import QThread
import urllib


class Download(QThread):
    def __init__(self, url, file_name, index, update_progress):
        QThread.__init__(self)
        self.url = url
        self.fileName = file_name
        self.id = index
        self.ProgressFunction = update_progress

    def run(self):
        print ("Running Thread url: " + str(self.url)
               + "\n\t\tfile name: " + str(self.fileName))
        testfile = urllib.URLopener()
        testfile.retrieve(self.url, self.fileName, self.ProgressFunction)

