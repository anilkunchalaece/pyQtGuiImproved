#Author : Kunchala Anil
#Date : Aug 27 2016
#Email : anilkunchalaece@gmail.com
#Import the Layout
from orgLayout import Ui_prepare2Pg
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
        self.setupLogic()
        self.data = TestData()
        self.maxQuestions = len(self.data.queDict)
        self.resultDict = { }
        self.selectedOption = 'n'
        self.addScrollArea()

    def addScrollArea(self):
        for i in range (25):
            btn = "scrollBtn"+str(i)
            btn = QtGui.QPushButton(ui.scrollAreaWidgetContents)
            btn.setText("Scroll")
            if i<=25:
                x = 0
                y = i
            elif i <= 50:
                x= 1
                y = i - 25
            
            
            ui.gridLayout.addWidget(btn,x,y)

    
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
    
