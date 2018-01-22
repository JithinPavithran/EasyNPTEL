from PyQt4 import QtGui
from PyQt4.QtGui import QIntValidator, QTableWidgetItem, QProgressBar
from PyQt4.QtCore import pyqtSignal, pyqtSlot
from PyQt4.QtGui import QMessageBox
import os
from course import Course
from download import DownloadQueue, DownloadFile
import downloadUI


class DownloadWindow(QtGui.QMainWindow):

    updateProgress = pyqtSignal(int, int, int, int)

    def __init__(self):
        super(DownloadWindow, self).__init__()
        self.ui = downloadUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.course = Course()
        self.downloadQueue = DownloadQueue()
        self.downloadQueue.start()
        self.setup()
        self.setupSignals()

    def setup(self):
        self.ui.reportBtn.setEnabled(False)
        self.ui.stopSelectionBtn.setEnabled(False)
        self.ui.courseNo.setValidator(QIntValidator(99999999, 1000000000))
        self.ui.courseNo.setFocus()
        self.ui.courseNo.paste()
        # self.autoSearch()
        self.ui.folderLE.setText(os.getcwd())

    def setupSignals(self):
        self.ui.courseNo.returnPressed.connect(self.ui.searchBtn.click)
        self.ui.searchBtn.clicked.connect(self.searchBtnClicked)
        self.ui.downloadBtn.clicked.connect(self.downloadBtnClicked)
        self.ui.stopBtn.clicked.connect(self.stopAllDownloads)
        self.ui.stopSelectionBtn.clicked.connect(self.stopDownloads)
        self.ui.folderBrowse.clicked.connect(self.browseFolder)
        self.updateProgress.connect(self.updateProgressSlot)

    def downloadBtnClicked(self):
        # TODO: disable search button till the downloads finish or stopped manually
        self.ui.downloadBtn.setText("Please wait...")
        self.ui.downloadBtn.setEnabled(False)
        QtGui.QApplication.processEvents()
        selected_range = self.ui.chapterTable.selectedRanges()
        selected_range = [i for r in selected_range
                          for i in range(r.topRow(), r.bottomRow() + 1)]
        # "selected_range" is a list of positions in table
        print "{} items selected".format(len(selected_range))
        for i in selected_range:
            index = i
            file = DownloadFile(self.course.getMp4UrlMirror(index),
                                self.get_file_path(index),
                                index,
                                lambda index, size, tot, i=index:
                                    self.updateProgress.emit(
                                        index, size, tot, i))
            pg = QProgressBar()
            pg.setRange(0, 100)
            pg.setValue(0)
            self.ui.chapterTable.setCellWidget(i, 1, pg)
            self.downloadQueue.addToQueue(file)
            print file.fileName + " Added to download queue"

        self.ui.downloadBtn.setText("Start Download")
        self.ui.downloadBtn.setEnabled(True)
        QtGui.QApplication.processEvents()

    def stopDownloads(self):
        # TODO: Remove
        pass
        # selected_range = self.ui.chapterTable.selectedRanges()
        # for thread in self.threads:
        #     if selected_range[0] == thread.id:
        #         thread.stopThread()
        #         selected_range.pop[0]

    def stopAllDownloads(self):
        print "Clearing all downloads (Current download is retained)"
        while not self.downloadQueue.downloadQueue.empty():
            file = self.downloadQueue.downloadQueue.get()
            print "Cleared {}".format(file.fileName)
            self.ui.chapterTable.removeCellWidget(file.index, 1)

    @pyqtSlot(int, int, int, int)
    def updateProgressSlot(self, number, size, tot, index):
        if tot == 0:
            print "Zero sized file received!\nServer might be down."
            return
        # print "number=", number, " index=", index
        self.ui.chapterTable.cellWidget(index, 1).setValue(
            number * size * 100 / tot)

    def searchBtnClicked(self):
        self.ui.searchBtn.setEnabled(False)
        self.ui.searchBtn.setText("Searching...")
        QtGui.QApplication.processEvents()
        self.populateCourseList()
        self.ui.searchBtn.setText("Search")
        self.ui.searchBtn.setEnabled(True)
        QtGui.QApplication.processEvents()

    def populateCourseList(self, suppress_error=False):
        if suppress_error:
            print 'Populating with Errors suppressed'
        course_no = str(self.ui.courseNo.text())
        if course_no is None or course_no == "":
            if not suppress_error:
                self.warn('Empty Course Number', 'Please enter course number')
            return
        try:
            chapter_list = self.course.getChapterList(course_no)
        except ValueError as v_err:
            if not suppress_error:
                if v_err.args[0] == "Invalid response from server":
                    self.warn('Server Error',
                              'Invalid response from server\n' +
                              'Response: {}'.format(v_err.args[1]) +
                              '\nPlease check your connection')
                if v_err.args[0] == "Empty chapter list":
                    self.warn('Course Error',
                              'Received empty chapter-list\n'
                              'Please check your course number')
            return
        except Exception as e:
            if not suppress_error:
                if e.message.split(':')[0] == 'HTTPError':
                    self.warn('Connection Error',
                              'Failed to reach server\n'
                              'Please check your connection')
            return

        self.ui.chapterTable.setRowCount(len(chapter_list))
        for i in range(len(chapter_list)):
            self.ui.chapterTable.setItem(i, 0, QTableWidgetItem(chapter_list[i]))
        self.ui.courseNameLabel.setText(self.course.getCourseName())

    def browseFolder(self):
        dialog = QtGui.QFileDialog(self)
        dialog.setFileMode(QtGui.QFileDialog.Directory)
        dialog.setDirectory(self.ui.folderLE.text())
        dialog.exec_()
        self.ui.folderLE.setText(dialog.selectedFiles()[0])

    def get_file_path(self, index):
        return os.path.join(str(self.ui.folderLE.text()),
                            (self.course.getFileName(index)))

    def warn(self, title, warning, button='Ok'):
        QMessageBox.warning(self, title, warning, button)

    def onLoad(self):
        # TODO: Connect to on load signal
        self.autoSearch()

    def autoSearch(self):
        self.populateCourseList(True)
