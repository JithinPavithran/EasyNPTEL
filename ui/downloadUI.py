# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 457)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 300))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.courseNo = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.courseNo.sizePolicy().hasHeightForWidth())
        self.courseNo.setSizePolicy(sizePolicy)
        self.courseNo.setMinimumSize(QtCore.QSize(0, 30))
        self.courseNo.setInputMask(_fromUtf8(""))
        self.courseNo.setMaxLength(9)
        self.courseNo.setObjectName(_fromUtf8("courseNo"))
        self.horizontalLayout_2.addWidget(self.courseNo)
        self.searchBtn = QtGui.QPushButton(self.centralwidget)
        self.searchBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.searchBtn.setObjectName(_fromUtf8("searchBtn"))
        self.horizontalLayout_2.addWidget(self.searchBtn)
        self.courseNameLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.courseNameLabel.sizePolicy().hasHeightForWidth())
        self.courseNameLabel.setSizePolicy(sizePolicy)
        self.courseNameLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.courseNameLabel.setFont(font)
        self.courseNameLabel.setObjectName(_fromUtf8("courseNameLabel"))
        self.horizontalLayout_2.addWidget(self.courseNameLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.chapterTable = QtGui.QTableWidget(self.centralwidget)
        self.chapterTable.setMinimumSize(QtCore.QSize(300, 120))
        self.chapterTable.setAutoFillBackground(True)
        self.chapterTable.setFrameShape(QtGui.QFrame.Panel)
        self.chapterTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.chapterTable.setAlternatingRowColors(True)
        self.chapterTable.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.chapterTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.chapterTable.setTextElideMode(QtCore.Qt.ElideNone)
        self.chapterTable.setObjectName(_fromUtf8("chapterTable"))
        self.chapterTable.setColumnCount(2)
        self.chapterTable.setRowCount(6)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.chapterTable.setItem(5, 0, item)
        self.chapterTable.horizontalHeader().setCascadingSectionResizes(False)
        self.chapterTable.horizontalHeader().setDefaultSectionSize(450)
        self.chapterTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.chapterTable)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.folderLabel = QtGui.QLabel(self.centralwidget)
        self.folderLabel.setObjectName(_fromUtf8("folderLabel"))
        self.horizontalLayout_5.addWidget(self.folderLabel)
        self.folderLE = QtGui.QLineEdit(self.centralwidget)
        self.folderLE.setObjectName(_fromUtf8("folderLE"))
        self.horizontalLayout_5.addWidget(self.folderLE)
        self.folderBrowse = QtGui.QPushButton(self.centralwidget)
        self.folderBrowse.setObjectName(_fromUtf8("folderBrowse"))
        self.horizontalLayout_5.addWidget(self.folderBrowse)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.reportBtn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reportBtn.sizePolicy().hasHeightForWidth())
        self.reportBtn.setSizePolicy(sizePolicy)
        self.reportBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.reportBtn.setMaximumSize(QtCore.QSize(110, 16777215))
        self.reportBtn.setObjectName(_fromUtf8("reportBtn"))
        self.horizontalLayout_3.addWidget(self.reportBtn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.stopBtn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopBtn.sizePolicy().hasHeightForWidth())
        self.stopBtn.setSizePolicy(sizePolicy)
        self.stopBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.stopBtn.setMaximumSize(QtCore.QSize(110, 16777215))
        self.stopBtn.setAutoFillBackground(False)
        self.stopBtn.setObjectName(_fromUtf8("stopBtn"))
        self.horizontalLayout_3.addWidget(self.stopBtn)
        self.stopSelectionBtn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopSelectionBtn.sizePolicy().hasHeightForWidth())
        self.stopSelectionBtn.setSizePolicy(sizePolicy)
        self.stopSelectionBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.stopSelectionBtn.setMaximumSize(QtCore.QSize(110, 16777215))
        self.stopSelectionBtn.setObjectName(_fromUtf8("stopSelectionBtn"))
        self.horizontalLayout_3.addWidget(self.stopSelectionBtn)
        self.downloadBtn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadBtn.sizePolicy().hasHeightForWidth())
        self.downloadBtn.setSizePolicy(sizePolicy)
        self.downloadBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.downloadBtn.setMaximumSize(QtCore.QSize(110, 16777215))
        self.downloadBtn.setObjectName(_fromUtf8("downloadBtn"))
        self.horizontalLayout_3.addWidget(self.downloadBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.courseNo.setPlaceholderText(_translate("MainWindow", "Course Number", None))
        self.searchBtn.setText(_translate("MainWindow", "Search", None))
        self.courseNameLabel.setText(_translate("MainWindow", "Course Name", None))
        item = self.chapterTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.chapterTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.chapterTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3", None))
        item = self.chapterTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4", None))
        item = self.chapterTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5", None))
        item = self.chapterTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6", None))
        item = self.chapterTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Chapter", None))
        item = self.chapterTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Download progress", None))
        __sortingEnabled = self.chapterTable.isSortingEnabled()
        self.chapterTable.setSortingEnabled(False)
        item = self.chapterTable.item(0, 0)
        item.setText(_translate("MainWindow", "Chapter 1", None))
        item = self.chapterTable.item(1, 0)
        item.setText(_translate("MainWindow", "chapter 2", None))
        item = self.chapterTable.item(2, 0)
        item.setText(_translate("MainWindow", "chapter 3", None))
        item = self.chapterTable.item(3, 0)
        item.setText(_translate("MainWindow", "chapter 4", None))
        item = self.chapterTable.item(4, 0)
        item.setText(_translate("MainWindow", "chapter 5", None))
        item = self.chapterTable.item(5, 0)
        item.setText(_translate("MainWindow", "chapter 6", None))
        self.chapterTable.setSortingEnabled(__sortingEnabled)
        self.folderLabel.setText(_translate("MainWindow", "Download folder: ", None))
        self.folderBrowse.setText(_translate("MainWindow", "Browse", None))
        self.reportBtn.setText(_translate("MainWindow", "Report a problem", None))
        self.stopBtn.setText(_translate("MainWindow", "Stop All", None))
        self.stopSelectionBtn.setText(_translate("MainWindow", "Stop selected", None))
        self.downloadBtn.setText(_translate("MainWindow", "Start Download", None))

