import sys, time
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("main.ui", self)
        self.test = 0
        self.timeout = time.time() + 5  # 5 s from now
        self.timer = QTimer()
        self.timer.timeout.connect(self.clear)
        self.timer.start(5000)
        self.lineEdit.textChanged.connect(self.reset_timer)

    def clear(self):
        self.lineEdit.clear()

    def reset_timer(self):
        self.timer.start(5000)
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
