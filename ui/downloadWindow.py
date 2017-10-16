from PyQt4 import QtGui, uic

from PyQt4.QtGui import QIntValidator, QTableWidgetItem,\
    QTableWidgetSelectionRange, QProgressBar, QWidget
from PyQt4.QtCore import pyqtSignal, pyqtSlot
from PyQt4.QtGui import QMessageBox

from course import Course
from download import Download
import downloadUI

from PyQt4.QtGui import QLineEdit

class DownloadWindow(QtGui.QMainWindow):

    updateProgress = pyqtSignal(int, int, int, int)
    threads = []

    def __init__(self):
        super(DownloadWindow, self).__init__()
        self.ui = downloadUI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.course = Course()
        self.threads = []

        self.setup()
        self.setupSignals()

    def autoSearch(self):
        self.ui.searchBtn.click()

    def setup(self):
        self.ui.courseNo.setValidator(QIntValidator(99999999, 1000000000))
        self.ui.courseNo.setFocus()
        self.ui.courseNo.paste()
        self.autoSearch()

    def setupSignals(self):
        self.ui.courseNo.returnPressed.connect(self.ui.searchBtn.click)
        self.ui.searchBtn.clicked.connect(self.populateCourseList)
        self.ui.downloadBtn.clicked.connect(self.downloadBtnClicked)
        self.ui.stopBtn.clicked.connect(self.stopAllDownloads)
        self.ui.stopSelectionBtn.clicked.connect(self.stopDownloads)
        self.updateProgress.connect(self.updateProgressSlot)

    def downloadBtnClicked(self):
        if False: # TODO: Download in progress
            print "Download in progress."
        selected_range = self.ui.chapterTable.selectedRanges()
        selected_range = [i for r in selected_range
                          for i in range(r.topRow(), r.bottomRow() + 1)]
        # selected_range is a list of positions in table
        for i in selected_range:
            pg = QProgressBar()
            pg.setRange(0, 100)
            pg.setValue(0)
            self.ui.chapterTable.setCellWidget(i, 1, pg)
            self.threads.append(
                Download(self.course.getMp4UrlMirror1(i),
                         "test/"+self.course.getFileName(i, "mp4"),
                         i,
                         lambda index, size, tot, i=i : self.updateProgress.emit(index, size, tot, i)
                         )
            )
            self.threads[-1].start()

        # for i in selected_range[:(5 if len(selected_range)>5 else len(selected_range))]:
        #     self.threads[i].start()

    def stopDownloads(self):
        selected_range = self.ui.chapterTable.selectedRanges()
        for thread in self.threads:
            if selected_range[0] == thread.id:
                thread.stopThread()
                selected_range.pop[0]

    def stopAllDownloads(self):
        for thread in self.threads:
            thread.stopThread()

    @pyqtSlot(int, int, int, int)
    def updateProgressSlot(self, number, size, tot, index):
        print "number=", number, " index=", index
        self.chapterTable.cellWidget(index, 1).setValue(
            number * size * 100 / tot)

    def populateCourseList(self):
        try:
            chapter_list = self.course.getChapterList(str(self.ui.courseNo.text()))
        except ValueError as v_err:
            if v_err.args[0] == "Invalid response from server":
                QMessageBox.warning(self, "Server Error",
                                    "Invalid response from server\n"
                                    "Response: " + str(v_err.args[1]) +
                                    "\n\nPlease Check your connection\n"
                                    "or Please report a problem if necessary")
            if v_err.args[0] == "Empty chapter list":
                QMessageBox.warning(self, "Course Error",
                                    "Received empty chapter list for the requested course!"
                                    "\nPlease double check the chapter number")

        self.ui.chapterTable.setRowCount(len(chapter_list))
        for i in range(len(chapter_list)):
            self.ui.chapterTable.setItem(i, 0, QTableWidgetItem(chapter_list[i]))
        self.ui.courseNameLabel.setText(self.course.getCourseName())

