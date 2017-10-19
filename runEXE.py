import subprocess
import time
import PyQt5

def initUI(self):
    navitPath = ""
    subprocess.Popen(navitPath)
    navWin = win32gui.FindWindowEx(0,0, "CalcFrame")
    time.sleep(0.05)
    window = QWindow.fromWinId(navWin)
    self.createWindowContainer(window,self)
    self.setGeometry(500, 500, 450, 400)
    self.setWindowTitle("Navigation')
    self.show()
