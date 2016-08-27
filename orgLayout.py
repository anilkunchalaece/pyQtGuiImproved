# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orgLayout.ui'
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

class Ui_prepare2Pg(object):
    def setupUi(self, prepare2Pg):
        prepare2Pg.setObjectName(_fromUtf8("prepare2Pg"))
        prepare2Pg.resize(1054, 777)
        self.centralwidget = QtGui.QWidget(prepare2Pg)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.medPg = QtGui.QLabel(self.centralwidget)
        self.medPg.setObjectName(_fromUtf8("medPg"))
        self.horizontalLayout.addWidget(self.medPg)
        self.testNameLabel = QtGui.QLabel(self.centralwidget)
        self.testNameLabel.setObjectName(_fromUtf8("testNameLabel"))
        self.horizontalLayout.addWidget(self.testNameLabel)
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setMaximumSize(QtCore.QSize(150, 70))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.QuestionLabel = QtGui.QLabel(self.centralwidget)
        self.QuestionLabel.setWordWrap(True)
        self.QuestionLabel.setObjectName(_fromUtf8("QuestionLabel"))
        self.horizontalLayout_4.addWidget(self.QuestionLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1021, 141))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.optARadioButton = QtGui.QRadioButton(self.widget)
        self.optARadioButton.setObjectName(_fromUtf8("optARadioButton"))
        self.verticalLayout_3.addWidget(self.optARadioButton)
        self.optBRadioButton = QtGui.QRadioButton(self.widget)
        self.optBRadioButton.setObjectName(_fromUtf8("optBRadioButton"))
        self.verticalLayout_3.addWidget(self.optBRadioButton)
        self.optCRadioButton = QtGui.QRadioButton(self.widget)
        self.optCRadioButton.setObjectName(_fromUtf8("optCRadioButton"))
        self.verticalLayout_3.addWidget(self.optCRadioButton)
        self.optDRadioButton = QtGui.QRadioButton(self.widget)
        self.optDRadioButton.setObjectName(_fromUtf8("optDRadioButton"))
        self.verticalLayout_3.addWidget(self.optDRadioButton)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.previousBtn = QtGui.QPushButton(self.centralwidget)
        self.previousBtn.setMaximumSize(QtCore.QSize(100, 70))
        self.previousBtn.setObjectName(_fromUtf8("previousBtn"))
        self.horizontalLayout_2.addWidget(self.previousBtn)
        self.nextBtn = QtGui.QPushButton(self.centralwidget)
        self.nextBtn.setMaximumSize(QtCore.QSize(100, 70))
        self.nextBtn.setObjectName(_fromUtf8("nextBtn"))
        self.horizontalLayout_2.addWidget(self.nextBtn)
        self.reviewBtn = QtGui.QPushButton(self.centralwidget)
        self.reviewBtn.setMaximumSize(QtCore.QSize(100, 70))
        self.reviewBtn.setObjectName(_fromUtf8("reviewBtn"))
        self.horizontalLayout_2.addWidget(self.reviewBtn)
        self.submitBtn = QtGui.QPushButton(self.centralwidget)
        self.submitBtn.setMaximumSize(QtCore.QSize(100, 70))
        self.submitBtn.setObjectName(_fromUtf8("submitBtn"))
        self.horizontalLayout_2.addWidget(self.submitBtn)
        self.endTestBtn = QtGui.QPushButton(self.centralwidget)
        self.endTestBtn.setMaximumSize(QtCore.QSize(100, 70))
        self.endTestBtn.setObjectName(_fromUtf8("endTestBtn"))
        self.horizontalLayout_2.addWidget(self.endTestBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.scrollArea = QtGui.QScrollArea(self.widget1)
        self.scrollArea.setGeometry(QtCore.QRect(-1, -1, 1041, 141))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1039, 139))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollBtn = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.scrollBtn.setObjectName(_fromUtf8("scrollBtn"))
        self.gridLayout.addWidget(self.scrollBtn, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.widget1)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        prepare2Pg.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(prepare2Pg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1054, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        prepare2Pg.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(prepare2Pg)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        prepare2Pg.setStatusBar(self.statusbar)

        self.retranslateUi(prepare2Pg)
        QtCore.QMetaObject.connectSlotsByName(prepare2Pg)

    def retranslateUi(self, prepare2Pg):
        prepare2Pg.setWindowTitle(_translate("prepare2Pg", "MainWindow", None))
        self.medPg.setText(_translate("prepare2Pg", "MED PG", None))
        self.testNameLabel.setText(_translate("prepare2Pg", "TEST NAME", None))
        self.QuestionLabel.setText(_translate("prepare2Pg", "This is a question ???", None))
        self.groupBox.setTitle(_translate("prepare2Pg", "GroupBox", None))
        self.optARadioButton.setText(_translate("prepare2Pg", "RadioButton", None))
        self.optBRadioButton.setText(_translate("prepare2Pg", "RadioButton", None))
        self.optCRadioButton.setText(_translate("prepare2Pg", "RadioButton", None))
        self.optDRadioButton.setText(_translate("prepare2Pg", "RadioButton", None))
        self.previousBtn.setText(_translate("prepare2Pg", "Previous", None))
        self.nextBtn.setText(_translate("prepare2Pg", "Next", None))
        self.reviewBtn.setText(_translate("prepare2Pg", "Mark for review", None))
        self.submitBtn.setText(_translate("prepare2Pg", "Submit", None))
        self.endTestBtn.setText(_translate("prepare2Pg", "End Test", None))
        self.scrollBtn.setText(_translate("prepare2Pg", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    prepare2Pg = QtGui.QMainWindow()
    ui = Ui_prepare2Pg()
    ui.setupUi(prepare2Pg)
    prepare2Pg.show()
    sys.exit(app.exec_())

