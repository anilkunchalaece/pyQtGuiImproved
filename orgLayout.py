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
        prepare2Pg.resize(1304, 777)
        self.centralwidget = QtGui.QWidget(prepare2Pg)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 390, 941, 211))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 1021, 191))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(-1, 6, -1, -1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.optARadioButton = QtGui.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.optARadioButton.setFont(font)
        self.optARadioButton.setObjectName(_fromUtf8("optARadioButton"))
        self.buttonGroup = QtGui.QButtonGroup(prepare2Pg)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.optARadioButton)
        self.verticalLayout_3.addWidget(self.optARadioButton)
        self.optBRadioButton = QtGui.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.optBRadioButton.setFont(font)
        self.optBRadioButton.setObjectName(_fromUtf8("optBRadioButton"))
        self.buttonGroup.addButton(self.optBRadioButton)
        self.verticalLayout_3.addWidget(self.optBRadioButton)
        self.optCRadioButton = QtGui.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.optCRadioButton.setFont(font)
        self.optCRadioButton.setObjectName(_fromUtf8("optCRadioButton"))
        self.buttonGroup.addButton(self.optCRadioButton)
        self.verticalLayout_3.addWidget(self.optCRadioButton)
        self.optDRadioButton = QtGui.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.optDRadioButton.setFont(font)
        self.optDRadioButton.setObjectName(_fromUtf8("optDRadioButton"))
        self.buttonGroup.addButton(self.optDRadioButton)
        self.verticalLayout_3.addWidget(self.optDRadioButton)
        self.layoutWidget.raise_()
        self.verticalLayout_5.addWidget(self.groupBox)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 120, 941, 261))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.QuestionLabel = QtGui.QLabel(self.widget1)
        self.QuestionLabel.setObjectName(_fromUtf8("QuestionLabel"))
        self.horizontalLayout_4.addWidget(self.QuestionLabel)
        self.widget2 = QtGui.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(10, 610, 941, 51))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.previousBtn = QtGui.QPushButton(self.widget2)
        self.previousBtn.setMaximumSize(QtCore.QSize(100, 70))
        self.previousBtn.setObjectName(_fromUtf8("previousBtn"))
        self.horizontalLayout_2.addWidget(self.previousBtn)
        self.nextBtn = QtGui.QPushButton(self.widget2)
        self.nextBtn.setMaximumSize(QtCore.QSize(100, 70))
        self.nextBtn.setObjectName(_fromUtf8("nextBtn"))
        self.horizontalLayout_2.addWidget(self.nextBtn)
        self.reviewBtn = QtGui.QPushButton(self.widget2)
        self.reviewBtn.setMaximumSize(QtCore.QSize(100, 70))
        self.reviewBtn.setObjectName(_fromUtf8("reviewBtn"))
        self.horizontalLayout_2.addWidget(self.reviewBtn)
        self.submitBtn = QtGui.QPushButton(self.widget2)
        self.submitBtn.setMaximumSize(QtCore.QSize(100, 70))
        self.submitBtn.setObjectName(_fromUtf8("submitBtn"))
        self.horizontalLayout_2.addWidget(self.submitBtn)
        self.endTestBtn = QtGui.QPushButton(self.widget2)
        self.endTestBtn.setMaximumSize(QtCore.QSize(100, 70))
        self.endTestBtn.setObjectName(_fromUtf8("endTestBtn"))
        self.horizontalLayout_2.addWidget(self.endTestBtn)
        self.widget3 = QtGui.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(9, 9, 1191, 111))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.medPg = QtGui.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.medPg.setFont(font)
        self.medPg.setObjectName(_fromUtf8("medPg"))
        self.horizontalLayout.addWidget(self.medPg)
        self.testNameLabel = QtGui.QLabel(self.widget3)
        self.testNameLabel.setObjectName(_fromUtf8("testNameLabel"))
        self.horizontalLayout.addWidget(self.testNameLabel)
        self.lcdNumber = QtGui.QLCDNumber(self.widget3)
        self.lcdNumber.setMaximumSize(QtCore.QSize(150, 70))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.widget4 = QtGui.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(950, 120, 261, 541))
        self.widget4.setObjectName(_fromUtf8("widget4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget5 = QtGui.QWidget(self.widget4)
        self.widget5.setObjectName(_fromUtf8("widget5"))
        self.scrollArea = QtGui.QScrollArea(self.widget5)
        self.scrollArea.setGeometry(QtCore.QRect(0, -2, 241, 541))
        self.scrollArea.setStyleSheet(_fromUtf8(""))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 222, 522))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.widget5)
        self.endTestBtn.raise_()
        prepare2Pg.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(prepare2Pg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1304, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        prepare2Pg.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(prepare2Pg)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        prepare2Pg.setStatusBar(self.statusbar)

        self.retranslateUi(prepare2Pg)
        QtCore.QMetaObject.connectSlotsByName(prepare2Pg)

    def retranslateUi(self, prepare2Pg):
        prepare2Pg.setWindowTitle(_translate("prepare2Pg", "MainWindow", None))
        self.groupBox.setTitle(_translate("prepare2Pg", "GroupBox", None))
        self.optARadioButton.setText(_translate("prepare2Pg", "RadioButton", None))
        self.optBRadioButton.setText(_translate("prepare2Pg", "RadioButton", None))
        self.optCRadioButton.setText(_translate("prepare2Pg", "RadioButton", None))
        self.optDRadioButton.setText(_translate("prepare2Pg", "RadioButton", None))
        self.QuestionLabel.setText(_translate("prepare2Pg", "TextLabel", None))
        self.previousBtn.setText(_translate("prepare2Pg", "Previous", None))
        self.nextBtn.setText(_translate("prepare2Pg", "Next", None))
        self.reviewBtn.setText(_translate("prepare2Pg", "Mark for review", None))
        self.submitBtn.setText(_translate("prepare2Pg", "Submit", None))
        self.endTestBtn.setText(_translate("prepare2Pg", "End Test", None))
        self.medPg.setText(_translate("prepare2Pg", "<html><head/><body><p align=\"center\"><span style=\" color:#ff5500;\">Prepare2Pg</span></p></body></html>", None))
        self.testNameLabel.setText(_translate("prepare2Pg", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#0000ff;\">Mock Test - 1</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    prepare2Pg = QtGui.QMainWindow()
    ui = Ui_prepare2Pg()
    ui.setupUi(prepare2Pg)
    prepare2Pg.show()
    sys.exit(app.exec_())

