from PyQt4 import QtGui, uic

from PyQt4.QtGui import QIntValidator, QTableWidgetItem, QTableWidgetSelectionRange, QProgressBar
from PyQt4.QtCore import pyqtSignal, pyqtSlot

from course import Course
from download import Download

from PyQt4.QtGui import QLineEdit

class DownloadWindow(QtGui.QMainWindow):

    updateProgress = pyqtSignal(int, int, int, int)

    def __init__(self):
        super(DownloadWindow, self).__init__()
        uic.loadUi("resources/download.ui", self)

        self.course = Course()
        self.threads = []

        self.setup()
        self.setupSignals()

    def autoSearch(self):
        self.searchBtn.click()

    def setup(self):
        self.courseNo.setValidator(QIntValidator(99999999, 1000000000))
        self.courseNo.setFocus()
        self.courseNo.paste()
        self.autoSearch()

    def setupSignals(self):
        self.courseNo.returnPressed.connect(self.searchBtn.click)
        self.searchBtn.clicked.connect(self.populateCourseList)
        self.selectAllBtn.clicked.connect(self.selectAllChapters)
        self.clearAllBtn.clicked.connect(self.clearAllSelection)
        self.downloadBtn.clicked.connect(self.downloadBtnClicked)
        self.updateProgress.connect(self.updateProgressSlot)

    def downloadBtnClicked(self):
        if False: # TODO: Download in progress
            print "Download in progress."
        selected_range = self.chapterTable.selectedRanges()
        selected_range = [i for r in selected_range
                          for i in range(r.topRow(), r.bottomRow() + 1)]
        for i in selected_range:
            pg = QProgressBar()
            pg.setRange(0, 100)
            pg.setValue(0)
            self.chapterTable.setCellWidget(i, 1, pg)
            self.threads.append(
                Download(self.course.getMp4UrlMirror1(i),
                         "test/"+self.course.getFileName(i, "mp4"),
                         i,
                         lambda index, size, tot, i=i : self.updateProgress.emit(index, size, tot, i)
                         )
            )
            self.threads[-1].start()

    @pyqtSlot(int, int, int, int)
    def updateProgressSlot(self, number, size, tot, index):
        print "number=", number, " index=", index
        self.chapterTable.cellWidget(index, 1).setValue(
            number * size * 100 / tot)

    def populateCourseList(self):
        print "Hai"
        chapter_list = self.course.getChapterList(str(self.courseNo.text()))
        print "Hello"
        self.chapterTable.setRowCount(len(chapter_list))
        for i in range(len(chapter_list)):
            self.chapterTable.setItem(i, 0, QTableWidgetItem(chapter_list[i]))
        self.courseNameLabel.setText(self.course.getCourseName())

    def selectAllChapters(self):
        self.chapterTable.setRangeSelected(
            QTableWidgetSelectionRange(0, 0, self.chapterTable.rowCount() - 1, 0), True)

    def clearAllSelection(self):
        self.chapterTable.setRangeSelected(
            QTableWidgetSelectionRange(0, 0, self.chapterTable.rowCount() - 1, 0), False)

