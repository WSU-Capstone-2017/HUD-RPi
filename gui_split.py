#Summary of Code: Includes the GUI for the split-screen functionality
#
#Language: Python
#Software Engineers: Akil, Nasser, Ridwan, Yosef

import sys
import time
from threading import Thread
import obd


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setMinimumSize(QtCore.QSize(320, 180))
        MainWindow.setMaximumSize(QtCore.QSize(480, 320))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MphLabel = QtWidgets.QLabel(self.centralwidget)
        self.MphLabel.setGeometry(QtCore.QRect(389, 40, 82, 50))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.MphLabel.setFont(font)
        self.MphLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"font: 75 italic 30pt \"OCR A Extended\";")
        self.MphLabel.setObjectName("MphLabel")
        self.speed_val = QtWidgets.QLabel(self.centralwidget)
        self.speed_val.setGeometry(QtCore.QRect(240, 20, 151, 61))
        self.speed_val.setStyleSheet("font: 75 60pt \"OCR A Extended\";\n"
"color: rgb(255, 255, 255);")
        self.speed_val.setObjectName("speed_val")
        self.labelRpm = QtWidgets.QLabel(self.centralwidget)
        self.labelRpm.setGeometry(QtCore.QRect(430, 110, 51, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.labelRpm.setFont(font)
        self.labelRpm.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelRpm.setObjectName("labelRpm")
        self.rpm_val = QtWidgets.QLabel(self.centralwidget)
        self.rpm_val.setGeometry(QtCore.QRect(240, 110, 181, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.rpm_val.setFont(font)
        self.rpm_val.setStyleSheet("color: rgb(255, 255, 255);")
        self.rpm_val.setObjectName("rpm_val")
        self.fuel_val = QtWidgets.QProgressBar(self.centralwidget)
        self.fuel_val.setGeometry(QtCore.QRect(340, 160, 131, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.fuel_val.setFont(font)
        self.fuel_val.setStyleSheet("color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.fuel_val.setProperty("value", 24)
        self.fuel_val.setObjectName("fuel_val")
        self.fuelLabel = QtWidgets.QLabel(self.centralwidget)
        self.fuelLabel.setGeometry(QtCore.QRect(270, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        font.setItalic(True)
        font.setUnderline(True)
        self.fuelLabel.setFont(font)
        self.fuelLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.fuelLabel.setObjectName("fuelLabel")
        self.alerts = QtWidgets.QTextBrowser(self.centralwidget)
        self.alerts.setGeometry(QtCore.QRect(260, 210, 211, 81))
        self.alerts.setStyleSheet("color: rgb(255, 255, 255);")
        self.alerts.setObjectName("alerts")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
###################################################### For QA
        th = Thread(target=self.instrument_readings) #
        th.start() #
#####################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MphLabel.setText(_translate("MainWindow", "Mph"))
        self.speed_val.setText(_translate("MainWindow", "100"))
        self.labelRpm.setText(_translate("MainWindow", "Rpm"))
        self.rpm_val.setText(_translate("MainWindow", "13000"))
        self.fuelLabel.setText(_translate("MainWindow", "FUEL"))
        self.alerts.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Oil Change Required</span></p></body></html>"))
######################################################## ForQA
    def instrument_readings(self):

             connection = obd.OBD()
             rpmCmd = obd.commands.RPM
             speedCmd = obd.commands.SPEED
             fuelCmd = obd.commands.FUEL_LEVEL
             while 1:
                fuelResponse = connection.query(fuelCmd)
                rpmResponse = connection.query(rpmCmd)
                speedResponse = connection.query(speedCmd)

                fuelString = str(fuelResponse.value).split()
                rpmString = str(rpmResponse.value).split()
                speedString = str(speedResponse.value).split()

                if fuelString[0] != "None":
                    fuel = float(fuelString[0])
                    self.fuel_val.setValue(fuel)
                
                if speedString[0] != "None":
                    speed = float(speedString[0]) * 0.62137119223733 # convert Kilometers per hour to MPH
                    self.speed_val.setText(str(speed))

                if rpmString[0] != "None":
                    rpm = float(rpmString[0])
                    self.rpm_val.setText(str(rpm))
                                     
######################################################################        
        
################################################ For QA
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui_window = Ui_MainWindow()
    gui_window.show()
    sys.exit(app.exec_())
######################################################
