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
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.fuelReading(MainWindow)#Grabs fuelReading def
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
############################ START
    def fuelReading(self):
        connection = obd.OBD() #connects to OBD-II
        fuelCmd = obd.commands.FUEL_LEVEL #Sets the OBD-II FUEL_LEVEL command 
        while 1:
            fuelResponse = connection.query(fuelCmd) #Connection query
            fuelString = str(fuelResponse.value).split() #Converts to string
            while fuelString[0] != "None":
                fuel = float(fuelString[0]) #converts to float
                if fuel <= 25:
                    self.progressBar_2.setProperty("value", 100) #If Fuel is <= 25% show one bar 
                elif fuel <= 50:
                    self.progressBar.setProperty("value", 100)#If Fuel is <= 25% show two bar 
                    self.progressBar_2.setProperty("value", 100)
                elif fuel <= 75:
                    self.progressBar_3.setProperty("value", 100)#If Fuel is <= 25% show three bar 
                    self.progressBar.setProperty("value", 100)
                    self.progressBar_2.setProperty("value", 100)
                elif fuel <= 100:
                    self.progressBar_4.setProperty("value", 100)#If Fuel is <= 25% show four bar 
                    self.progressBar_3.setProperty("value", 100)
                    self.progressBar.setProperty("value", 100)
                    self.progressBar_2.setProperty("value", 100)
                
########################### FINISH
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui_window = Ui_MainWindow()
    gui_window.show()
    sys.exit(app.exec_())

