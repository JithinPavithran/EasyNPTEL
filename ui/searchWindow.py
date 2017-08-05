from PyQt4 import QtGui, uic

from course import Course


class SearchWindow(QtGui.QMainWindow):

    def __init__(self):
        super(SearchWindow, self).__init__()
        uic.loadUi("resources/search.ui", self)
        self.setupSignals()

    def setupSignals(self):
        self.searchText.textChanged.connect(self.populateCourseList)

    def populateCourseList(self):
        if len(self.searchText.text()) > 3 :
            list = Course.searchCourse(self.searchText.text())
            self.courseList.clear()
            self.courseList.addItems(list)