import sys
from ui.downloadWindow import DownloadWindow
from PyQt4 import QtCore, QtGui

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = DownloadWindow()
    GUI.show()
    sys.exit(app.exec_())

run()