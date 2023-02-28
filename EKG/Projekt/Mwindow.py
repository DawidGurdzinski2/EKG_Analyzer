from PyQt5 import QtCore, QtGui, QtWidgets
from Algorithms import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        self.al=Algorithms()
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.BtnCSV = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCSV.setGeometry(QtCore.QRect(60, 20, 141, 71))
        self.BtnCSV.setObjectName("BtnCSV")
        self.BtnCSV.clicked.connect(self.LoadCSV)
        
        self.BtnPKL = QtWidgets.QPushButton(self.centralwidget)
        self.BtnPKL.setGeometry(QtCore.QRect(60, 110, 141, 71))
        self.BtnPKL.setObjectName("BtnPKL")
        self.BtnPKL.clicked.connect(self.LoadPKL)
        
        self.BtnWFBD = QtWidgets.QPushButton(self.centralwidget)
        self.BtnWFBD.setGeometry(QtCore.QRect(60, 210, 141, 71))
        self.BtnWFBD.setObjectName("BtnWFBD")
        self.BtnWFBD.clicked.connect(self.LoadWFBD)
        
        self.MeanRR = QtWidgets.QLabel(self.centralwidget)
        self.MeanRR.setGeometry(QtCore.QRect(360, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MeanRR.setFont(font)
        self.MeanRR.setObjectName("MeanRR")
        self.MeanBMP = QtWidgets.QLabel(self.centralwidget)
        self.MeanBMP.setGeometry(QtCore.QRect(370, 120, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.MeanBMP.setFont(font)
        self.MeanBMP.setObjectName("MeanBMP")
        self.SDNN = QtWidgets.QLabel(self.centralwidget)
        self.SDNN.setGeometry(QtCore.QRect(330, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SDNN.setFont(font)
        self.SDNN.setObjectName("SDNN")
        self.RMSSD = QtWidgets.QLabel(self.centralwidget)
        self.RMSSD.setGeometry(QtCore.QRect(340, 220, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RMSSD.setFont(font)
        self.RMSSD.setObjectName("RMSSD")
        self.NN50 = QtWidgets.QLabel(self.centralwidget)
        self.NN50.setGeometry(QtCore.QRect(320, 270, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NN50.setFont(font)
        self.NN50.setObjectName("NN50")
        self.TITLE = QtWidgets.QLabel(self.centralwidget)
        self.TITLE.setGeometry(QtCore.QRect(290, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TITLE.setFont(font)
        self.TITLE.setObjectName("TITLE")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 120, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 270, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BtnCSV.setText(_translate("MainWindow", "Load CSV"))
        self.BtnPKL.setText(_translate("MainWindow", "Load PKL"))
        self.BtnWFBD.setText(_translate("MainWindow", "Load WFBD"))
        self.MeanRR.setText(_translate("MainWindow", "0"))
        self.MeanBMP.setText(_translate("MainWindow", "0"))
        self.SDNN.setText(_translate("MainWindow", "0"))
        self.RMSSD.setText(_translate("MainWindow", "0"))
        self.NN50.setText(_translate("MainWindow", "0"))
        self.TITLE.setText(_translate("MainWindow", "Parameters"))
        self.label.setText(_translate("MainWindow", "Mean R-R: "))
        self.label_2.setText(_translate("MainWindow", "MEAN BPM:"))
        self.label_3.setText(_translate("MainWindow", "SDNN:"))
        self.label_4.setText(_translate("MainWindow", "RMSSD:"))
        self.label_5.setText(_translate("MainWindow", "NN50:"))

    def setParameters(self):
        self.MeanBMP.setText(str(round(self.al.MeanBMP,2))+" [bpm]")
        self.MeanRR.setText(str(round(self.al.MeanR_R,2))+" [ms]")
        self.SDNN.setText(str(round(self.al.SDNN,2))+" [ms]")
        self.RMSSD.setText(str(round(self.al.RMSSD,2))+" [ms]")
        self.NN50.setText(str(round(self.al.NN50,2))+" numbers")
        self.updateLabels()
    
    def updateLabels(self):
        self.MeanBMP.adjustSize()
        self.MeanRR.adjustSize()
        self.SDNN.adjustSize()
        self.RMSSD.adjustSize()
        self.NN50.adjustSize()
         
    def LoadCSV(self):
        try:
            app=QApplication(sys.argv)
            win = QMainWindow()
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(win,"QFileDialog.getOpenFileName()", "","*.csv", options=options)
            self.al.loadFileCsv(fileName)      
            self.setParameters()
        except:
            pass
            
        
    def LoadPKL(self):
        try:
            app=QApplication(sys.argv)
            win = QMainWindow()
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(win,"QFileDialog.getOpenFileName()", "","*.pkl", options=options)
            self.al.loadFilePkl(fileName)
            self.setParameters()
        except:
            pass
        
    def LoadWFBD(self): 
        try:
            app=QApplication(sys.argv)
            win = QMainWindow()
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(win,"QFileDialog.getOpenFileName()", "","*.dat", options=options)
            fileName=fileName[:len(fileName)-4]
            self.al.loadFileWfbd(fileName)
            self.setParameters()
        except:
            pass