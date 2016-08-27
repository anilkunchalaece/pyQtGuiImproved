#Author : Kunchala Anil
#Date : 27 Aug 2016
#Email : anilkunchalaece@gmail.com

#Check the Automatic Button Genration Clearly Ref guiAnilV3.py

#Import the Layout
from orgLayout import Ui_prepare2Pg
#import csv for TestData
import csv
#import the TestData
from testData import TestData
#Import the PyQt Core and Gui Libraries
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


class guiLogic(Ui_prepare2Pg):
    def __init__(self):
        self.questionIndex = 1
        self.data = TestData()
        self.maxQuestions = len(self.data.queDict)
        self.rows = 10
        self.rowAddition = self.rows
        self.resultDict = { }
        self.selectedOption = 'n'
        self.x = 0
        self.y = 0
        self.btn = {}

        self.addScrollArea()
        self.setupLogic()

    def addScrollArea(self):
        for key in range (len(self.data.keys)):
            self.btnKey = str(key+1)
            self.btn[self.btnKey] = QtGui.QPushButton(ui.scrollAreaWidgetContents)
            self.btnText = str(key+1)
            self.btn[self.btnKey].setText(self.btnText)
            self.btn[self.btnKey].setCheckable(True)
            self.btn[self.btnKey].toggle()
            self.btn[self.btnKey].clicked.connect(self.scrollFcn)
        
            if key < self.rows:
                if key == 0:
                    self.y = 0
                    self.x = 0
                else:
                    self.y = self.y + 1

            else:
                self.x = self.x+1
                self.y = 0
                self.rows = self.rows + self.rowAddition
#           print "x" + str(self.x)
#            print "y" + str(self.y)
#            print "key" + str(key)
#            print "self.rows" + str(self.rows)
            
            ui.gridLayout.addWidget(self.btn[self.btnKey],self.x,self.y)
#            print self.btn[self.btnKey]

    def scrollFcn(self):
        print "Scroll Btn Clicked"
        print MainWindow.sender().text() #this will grab the Pushbutton Reference Object From Mainwindow which is used to access the Btn Data
        #when the scroll Btn is Pressed with Reference Key Id call retranslateUi with key function
        self.retranslateUi(MainWindow.sender().text())

    
    def setupLogic(self):
        

        ui.nextBtn.setCheckable(True)
        ui.nextBtn.toggle()
        ui.nextBtn.clicked.connect(self.nextFcn)

        ui.reviewBtn.setCheckable(True)
        ui.reviewBtn.toggle()
        ui.reviewBtn.clicked.connect(self.reviewFcn)

        ui.submitBtn.setCheckable(True)
        ui.submitBtn.toggle()
        ui.submitBtn.clicked.connect(self.submitFcn)

        ui.endTestBtn.setCheckable(True)
        ui.endTestBtn.toggle()
        ui.endTestBtn.clicked.connect(self.endTestFcn)

        ui.previousBtn.setCheckable(True)
        ui.previousBtn.toggle()
        ui.previousBtn.clicked.connect(self.previousFcn)

        


    def nextFcn(self):
        print "Next Btn Selected"
        self.questionIndex=newLogic.questionIndex+1
        if self.questionIndex > self.maxQuestions :
            self.questionIndex = 1
        self.retranslateUi(newLogic.questionIndex)

    def reviewFcn(self):
        print "Review Btn Pressed"
        self.changeColor(self.questionIndex)

    def changeColor(self,Qindex):
#        print self.btn[str(Qindex)]
        self.btn[str(Qindex)].setStyleSheet("background-color: red")

    def submitFcn(self):
        print "Submit Btn Pressed"

        if ui.optARadioButton.isChecked():
            print "Option A is Selected"
            self.selectedOption = 'A'
        elif ui.optBRadioButton.isChecked():
            print "Option Bis Selected"
            self.selectedOption = 'B'
        elif ui.optCRadioButton.isChecked():
            print "Option C is Selected"
            self.selectedOption = 'C'
        elif ui.optDRadioButton.isChecked():
            print"Option D is Selected"
            self.selectedOption = 'D'
        else:
            print "No Option selected"
            self.selectedOption = 'N'
        self.resultDict[self.questionIndex] = self.selectedOption
        
    def endTestFcn(self):
        print "endTest Btn Pressed"
        print "Output Dict is "
        print self.resultDict

    def previousFcn(self):
        print "Previous Btn Pressed"
        newLogic.questionIndex=newLogic.questionIndex-1
        if self.questionIndex == 0:
            self.questionIndex = self.maxQuestions
            
        newLogic.retranslateUi(newLogic.questionIndex)

    def retranslateUi(self,QIndex):
        ui.testNameLabel.setText(_translate("prepare2Pg", "TEST NAME", None))
        ui.QuestionLabel.setText(_translate("prepare2Pg", newLogic.data.queDict[str(QIndex)], None))
        ui.optARadioButton.setText(_translate("prepare2Pg", newLogic.data.optADict[str(QIndex)], None))
        ui.optBRadioButton.setText(_translate("prepare2Pg", newLogic.data.optBDict[str(QIndex)], None))
        ui.optCRadioButton.setText(_translate("prepare2Pg", newLogic.data.optCDict[str(QIndex)], None))
        ui.optDRadioButton.setText(_translate("prepare2Pg", newLogic.data.optDDict[str(QIndex)], None))
        
        
        ui.optARadioButton.setChecked(False)
        ui.optBRadioButton.setChecked(False)
        ui.optCRadioButton.setChecked(False)
        ui.optDRadioButton.setChecked(False)
                  
        



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_prepare2Pg()
    ui.setupUi(MainWindow)
    MainWindow.show()

    newLogic = guiLogic()
    newLogic.retranslateUi(newLogic.questionIndex)
    
    sys.exit(app.exec_())
    
