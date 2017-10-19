import sys
import time
from threading import Thread
#import obd

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setMinimumSize(QtCore.QSize(320, 240))
        MainWindow.setMaximumSize(QtCore.QSize(480, 320))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rpm_val = QtWidgets.QLCDNumber(self.centralwidget)
        self.rpm_val.setGeometry(QtCore.QRect(200, 30, 131, 71))
        self.rpm_val.setStyleSheet("color: rgb(255, 255, 255);")
        self.rpm_val.setProperty("intValue", 13000)
        self.rpm_val.setObjectName("rpm_val")
        self.speed_val = QtWidgets.QLCDNumber(self.centralwidget)
        self.speed_val.setGeometry(QtCore.QRect(20, 20, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.speed_val.setFont(font)
        self.speed_val.setStyleSheet("color: rgb(255, 255, 255);")
        self.speed_val.setDigitCount(3)
        self.speed_val.setProperty("intValue", 100)
        self.speed_val.setObjectName("speed_val")
        self.mileage_val = QtWidgets.QLCDNumber(self.centralwidget)
        self.mileage_val.setGeometry(QtCore.QRect(0, 190, 201, 41))
        self.mileage_val.setStyleSheet("color: rgb(255, 255, 255);")
        self.mileage_val.setDigitCount(6)
        self.mileage_val.setProperty("intValue", 350000)
        self.mileage_val.setObjectName("mileage_val")
        self.fuel_val = QtWidgets.QProgressBar(self.centralwidget)
        self.fuel_val.setGeometry(QtCore.QRect(390, 40, 41, 201))
        self.fuel_val.setStyleSheet("color: rgb(255, 255, 255);")
        self.fuel_val.setProperty("value", 24)
        self.fuel_val.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fuel_val.setTextVisible(True)
        self.fuel_val.setOrientation(QtCore.Qt.Vertical)
        self.fuel_val.setInvertedAppearance(False)
        self.fuel_val.setObjectName("fuel_val")
        self.speed = QtWidgets.QLabel(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(40, 110, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.speed.setFont(font)
        self.speed.setStyleSheet("color: rgb(255, 255, 255);")
        self.speed.setFrameShadow(QtWidgets.QFrame.Plain)
        self.speed.setLineWidth(8)
        self.speed.setTextFormat(QtCore.Qt.AutoText)
        self.speed.setObjectName("speed")
        self.rpm = QtWidgets.QLabel(self.centralwidget)
        self.rpm.setGeometry(QtCore.QRect(240, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.rpm.setFont(font)
        self.rpm.setStyleSheet("color: rgb(255, 255, 255);")
        self.rpm.setObjectName("rpm")
        self.fuel = QtWidgets.QLabel(self.centralwidget)
        self.fuel.setGeometry(QtCore.QRect(360, 250, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.fuel.setFont(font)
        self.fuel.setStyleSheet("color: rgb(255, 255, 255);")
        self.fuel.setObjectName("fuel")
        self.mileage = QtWidgets.QLabel(self.centralwidget)
        self.mileage.setGeometry(QtCore.QRect(60, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.mileage.setFont(font)
        self.mileage.setStyleSheet("color: rgb(255, 255, 255);")
        self.mileage.setObjectName("mileage")
        self.alerts_val = QtWidgets.QTextBrowser(self.centralwidget)
        self.alerts_val.setGeometry(QtCore.QRect(210, 170, 121, 71))
        self.alerts_val.setStyleSheet("color: rgb(255, 170, 0);")
        self.alerts_val.setObjectName("alerts_val")
        self.alerts = QtWidgets.QLabel(self.centralwidget)
        self.alerts.setGeometry(QtCore.QRect(230, 250, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.alerts.setFont(font)
        self.alerts.setStyleSheet("color: rgb(255, 255, 255);")
        self.alerts.setObjectName("alerts")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

##################################################### For QA
        th = Thread(target=self.instrument_readings) #progress bar moves
        th.start()
##################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.speed.setText(_translate("MainWindow", "MPH"))
        self.rpm.setText(_translate("MainWindow", "RPM"))
        self.fuel.setText(_translate("MainWindow", "Fuel Level"))
        self.mileage.setText(_translate("MainWindow", "Mileage"))
        self.alerts_val.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Check Engine</span></p></body></html>"))
        self.alerts.setText(_translate("MainWindow", "Alerts"))
########################################### For QA
    def instrument_readings(self):
        x = 0
        
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
                # convert Kilometers per hour to Miles per hour
                speed = float(speedString[0]) * 0.62137119223733 
                self.speed_val.display(speed)

            if rpmString[0] != "None":
                rpm = float(rpmString[0])
                self.rpm_val.display(rpm)
                                     
####################################################################        
        

############################################### For QA
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui_window = Ui_MainWindow()
    gui_window.show()
    sys.exit(app.exec_())
###############################################################
