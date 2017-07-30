from course.course import Course
from PyQt4 import QtGui, QtCore, uic


class DownloadWindow(QtGui.QMainWindow):

    def __init__(self):
        super(DownloadWindow, self).__init__()
        uic.loadUi("resources/download.ui", self)
        self.setupSignals()

    def setupSignals(self):
        self.courseNo.returnPressed.connect(self.searchBtn.click)
        self.searchBtn.clicked.connect(self.populateCourseList)
        self.selectAllBtn.clicked.connect(self.selectAllChapters)
        self.clearAllBtn.clicked.connect(self.clearAllSelection)

    def populateCourseList(self):
        list = Course.getChapterList(self.courseNo.text())
        self.chapterList.clear()
        self.chapterList.addItems(list)

    def selectAllChapters(self):
        for i in xrange(self.chapterList.count()):
            self.chapterList.setItemSelected(self.chapterList.item(i), True)

    def clearAllSelection(self):
        for i in self.chapterList.selectedItems():
            self.chapterList.setItemSelected(i, False)