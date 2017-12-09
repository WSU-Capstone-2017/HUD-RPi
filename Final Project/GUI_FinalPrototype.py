import sys
import time
from threading import Thread
import os
import subprocess
import urllib
import webbrowser
import obd

alertDis = ""
os.system("sudo rfcomm connect hci0 00:1d:a5:00:29:c0")
os.system("sudo chmod 777 /dev/ttyUSB0")
os.system("sudo chmod 777 /var/www/html")
connection = obd.OBD("/dev/rfcomm0")

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_SplitWin(QtWidgets.QMainWindow):
    #  added parent
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
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
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(40, 240, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton1.setObjectName("pushButton1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "Switch Screen"))

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    # i added parent
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # when clicked
        self.pushButton1.clicked.connect(self.buttonHandler)
        self.pushButton3.clicked.connect(self.buttonHandler2)

       
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(320, 240))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
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
        self.rpm_val.setGeometry(QtCore.QRect(210, 55, 300, 100))#rpm value 200, 30, 131, 71
        self.rpm_val.setStyleSheet("color: rgb(255, 255, 255);")
        self.rpm_val.setProperty("intValue", 13000)
        self.rpm_val.setObjectName("rpm_val")
        self.speed_val = QtWidgets.QLCDNumber(self.centralwidget)
        self.speed_val.setGeometry(QtCore.QRect(20, 20, 180, 150))#speed value 20, 20, 161, 81
        font = QtGui.QFont()
        font.setPointSize(11)
        self.speed_val.setFont(font)
        self.speed_val.setStyleSheet("color: rgb(255, 255, 255);")
        self.speed_val.setDigitCount(3)
        self.speed_val.setProperty("intValue", 100)
        self.speed_val.setObjectName("speed_val")
        
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(520, 310, 90, 20))
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(520, 280, 90, 20))
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setObjectName("progressBar_2")

        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(520, 250, 90, 20))
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setObjectName("progressBar_3")
        
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(520, 220, 90, 20))
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setObjectName("progressBar_4")

        self.progressBar_5 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_5.setGeometry(QtCore.QRect(520, 190, 90, 20))
        self.progressBar_5.setTextVisible(False)
        self.progressBar_5.setObjectName("progressBar_5")

        self.progressBar_6 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_6.setGeometry(QtCore.QRect(520, 160, 90, 20))
        self.progressBar_6.setTextVisible(False)
        self.progressBar_6.setObjectName("progressBar_6")

        self.progressBar_7 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_7.setGeometry(QtCore.QRect(520, 130, 90, 20))
        self.progressBar_7.setTextVisible(False)
        self.progressBar_7.setObjectName("progressBar_7")

        self.progressBar_8 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_8.setGeometry(QtCore.QRect(520, 100, 90, 20))
        self.progressBar_8.setTextVisible(False)
        self.progressBar_8.setObjectName("progressBar_8")

        self.progressBar_9 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_9.setGeometry(QtCore.QRect(520, 70, 90, 20))
        self.progressBar_9.setTextVisible(False)
        self.progressBar_9.setObjectName("progressBar_9")

        self.progressBar_10 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_10.setGeometry(QtCore.QRect(520, 40, 90, 20))
        self.progressBar_10.setTextVisible(False)
        self.progressBar_10.setObjectName("progressBar_10")

        
        self.speed = QtWidgets.QLabel(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(140, 160, 150, 31))#MPH font 90, 110, 141, 31
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
        self.rpm.setGeometry(QtCore.QRect(428, 160, 70, 31))#RPM font 240, 110, 111, 31
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.rpm.setFont(font)
        self.rpm.setStyleSheet("color: rgb(255, 255, 255);")
        self.rpm.setObjectName("rpm")
        self.fuel = QtWidgets.QLabel(self.centralwidget)
        self.fuel.setGeometry(QtCore.QRect(510, 350, 120, 30))#fuel 
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.fuel.setFont(font)
        self.fuel.setStyleSheet("color: rgb(255, 255, 255);")
        self.fuel.setObjectName("fuel")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(60, 280, 175, 41)) #Online Navigation
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton3.setObjectName("pushButton3")
        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(60, 345, 175, 41)) #switch
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton1.setObjectName("pushButton1")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(300, 345, 150, 40)) #alerts
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton2.setObjectName("pushButton2")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(280, 230, 200, 100)) #textbox 280, 250, 170, 71
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        test = self.alert_reading() #Display Check engine message
        self.textEdit.setText(test)
        print test
##################################################### For QA
        th = Thread(target=self.instrument_readings) #Thread
        th.start()
##################################################################

##################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.speed.setText(_translate("MainWindow", "MPH"))
        self.rpm.setText(_translate("MainWindow", "RPM"))
        self.fuel.setText(_translate("MainWindow", "Fuel Level"))

        self.pushButton3.setText(_translate("MainWindow", "Online NAV"))        
        self.pushButton1.setText(_translate("MainWindow", "NavIT"))
        self.pushButton2.setText(_translate("MainWindow", "Alerts"))
###########################################################################
#switch screen handler for Online Navigation
    def buttonHandler2(self):
        os.system("DISPLAY=:0 chromium-browser -kiosk http://127.0.0.1/FinalOnlineNavigation.html")
        #os.system("DISPLAY=:0 chromium-browser http://127.0.0.1/prototype2_draft5.html")

       
#########################################################################
# switch screen handler for Navit
    def buttonHandler(self):

        
        navitPath= "navit"#"/usr/share/applications/navit.desktop"
        subprocess.Popen(navitPath)
        window = QWindow.fromWinId(navWin)
        self.createWindowContainer(window,self)
        self.setGeometry(500, 500, 450, 400)
        self.setWindowTitle("Navigation")
        self.mdiArea() #show()
        #os.system('navit')
    
########################################### For QA
    def alert_reading(self):
        global alertDis
        alertcmd = obd.commands.GET_DTC
        alert_resp = connection.query(alertcmd).value
        alert_str = str(alert_resp)
        alertDis = str(alert_str[3:len(alert_str)-3])
        
        print alertDis

        return alertDis
    def instrument_readings(self):

        x = 0
      
       # connection = obd.OBD("/dev/rfcomm0")
        
        rpmCmd = obd.commands.RPM
        speedCmd = obd.commands.SPEED
        fuelCmd = obd.commands.FUEL_LEVEL

        while True:
           
            fuelResponse = connection.query(fuelCmd)
            rpmResponse = connection.query(rpmCmd)
            speedResponse = connection.query(speedCmd)

            
            fuelString = str(fuelResponse.value).split()
            rpmString = str(rpmResponse.value).split()
            speedString = str(speedResponse.value).split()


            if fuelString[0] != "None":
                fuel = float(fuelString[0])
                if fuel <= 10:
                    self.progressBar.setProperty("value", 100)
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
    #gui_window.showMaximized()
    gui_window.showFullScreen()
    sys.exit(app.exec_())
###############################################################
