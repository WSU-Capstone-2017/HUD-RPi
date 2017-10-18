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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(360, 330, 71, 23))
        #self.progressBar.setProperty("value", 100)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(360, 360, 71, 23))
        #self.progressBar_2.setProperty("value", 100)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setObjectName("progressBar_2")
        
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(360, 300, 71, 23))
        #self.progressBar_3.setProperty("value", 100)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setObjectName("progressBar_3")
        
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(360, 270, 71, 23))
        #self.progressBar_4.setProperty("value", 100)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setObjectName("progressBar_4")

        self.progressBar_5 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_5.setGeometry(QtCore.QRect(360, 240, 71, 23))
        #self.progressBar_5.setProperty("value", 100)
        self.progressBar_5.setTextVisible(False)
        self.progressBar_5.setObjectName("progressBar_5")

        self.progressBar_6 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_6.setGeometry(QtCore.QRect(360, 210, 71, 23))
        #self.progressBar_6.setProperty("value", 100)
        self.progressBar_6.setTextVisible(False)
        self.progressBar_6.setObjectName("progressBar_6")

        self.progressBar_7 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_7.setGeometry(QtCore.QRect(360, 180, 71, 23))
        #self.progressBar_7.setProperty("value", 100)
        self.progressBar_7.setTextVisible(False)
        self.progressBar_7.setObjectName("progressBar_7")

        self.progressBar_8 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_8.setGeometry(QtCore.QRect(360, 150, 71, 23))
        #self.progressBar_8.setProperty("value", 100)
        self.progressBar_8.setTextVisible(False)
        self.progressBar_8.setObjectName("progressBar_8")

        self.progressBar_9 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_9.setGeometry(QtCore.QRect(360, 120, 71, 23))
        #self.progressBar_9.setProperty("value", 100)
        self.progressBar_9.setTextVisible(False)
        self.progressBar_9.setObjectName("progressBar_9")

        self.progressBar_10 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_10.setGeometry(QtCore.QRect(360, 90, 71, 23))
        #self.progressBar_10.setProperty("value", 100)
        self.progressBar_10.setTextVisible(False)
        self.progressBar_10.setObjectName("progressBar_10")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.fuelReading(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def fuelReading(self, MainWindow):
        #connection = obd.OBD()
        #fuelCmd = obd.commands.FUEL_LEVEL
        #while 1:
            #fuelResponse = connection.query(fuelCmd)
            #fuelString = str(fuelResponse.value).split()
            #while fuelString[0] != "None":
                #fuel = float(fuelString[0])
        fuel = 33
        if fuel <= 10:
            self.progressBar_2.setProperty("value", 100)
        elif fuel <= 20:
            self.progressBar.setProperty("value", 100)
            self.progressBar_2.setProperty("value", 100)
        elif fuel <= 30:
            self.progressBar_3.setProperty("value", 100)
            self.progressBar.setProperty("value", 100)
            self.progressBar_2.setProperty("value", 100)
        elif fuel <= 40:
            self.progressBar_4.setProperty("value", 100)
            self.progressBar_3.setProperty("value", 100)
            self.progressBar.setProperty("value", 100)
            self.progressBar_2.setProperty("value", 100)
        elif fuel <= 50:
            self.progressBar_5.setProperty("value", 100)
            self.progressBar_4.setProperty("value", 100)
            self.progressBar_3.setProperty("value", 100)
            self.progressBar.setProperty("value", 100)
            self.progressBar_2.setProperty("value", 100)
        elif fuel <= 60:
            self.progressBar_6.setProperty("value", 100)
            self.progressBar_5.setProperty("value", 100)
            self.progressBar_4.setProperty("value", 100)
            self.progressBar_3.setProperty("value", 100)
            self.progressBar.setProperty("value", 100)
            self.progressBar_2.setProperty("value", 100)
        elif fuel <= 70:
            self.progressBar_7.setProperty("value", 100)
            self.progressBar_6.setProperty("value", 100)
            self.progressBar_5.setProperty("value", 100)
            self.progressBar_4.setProperty("value", 100)
            self.progressBar_3.setProperty("value", 100)
            self.progressBar.setProperty("value", 100)
            self.progressBar_2.setProperty("value", 100)
        elif fuel <= 80:
            self.progressBar_8.setProperty("value", 100)
            self.progressBar_7.setProperty("value", 100)
            self.progressBar_6.setProperty("value", 100)
            self.progressBar_5.setProperty("value", 100)
            self.progressBar_4.setProperty("value", 100)
            self.progressBar_3.setProperty("value", 100)
            self.progressBar.setProperty("value", 100)
            self.progressBar_2.setProperty("value", 100)
        elif fuel <= 90:
            self.progressBar_9.setProperty("value", 100)
            self.progressBar_8.setProperty("value", 100)
            self.progressBar_7.setProperty("value", 100)
            self.progressBar_6.setProperty("value", 100)
            self.progressBar_5.setProperty("value", 100)
            self.progressBar_4.setProperty("value", 100)
            self.progressBar_3.setProperty("value", 100)
            self.progressBar.setProperty("value", 100)
            self.progressBar_2.setProperty("value", 100)
        elif fuel <= 100:
            self.progressBar_10.setProperty("value", 100)
            self.progressBar_9.setProperty("value", 100)
            self.progressBar_8.setProperty("value", 100)
            self.progressBar_7.setProperty("value", 100)
            self.progressBar_6.setProperty("value", 100)
            self.progressBar_5.setProperty("value", 100)
            self.progressBar_4.setProperty("value", 100)
            self.progressBar_3.setProperty("value", 100)
            self.progressBar.setProperty("value", 100)
            self.progressBar_2.setProperty("value", 100)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui_window = Ui_MainWindow()
    gui_window.show()
    sys.exit(app.exec_())
