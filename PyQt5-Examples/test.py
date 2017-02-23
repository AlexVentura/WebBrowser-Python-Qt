#!/usr/bin/python3

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import (QFont, QIcon)
from PyQt5.QtWidgets import (QApplication, QMainWindow)

class Test(QMainWindow):
    def __init__(self):
        super(Test, self).__init__()

#        self.ui = uic.loadUi("test-ok.ui", self)
        self.ui = uic.loadUi("main.ui", self)

    @pyqtSlot()
    def calculate(self):
        print("Calc")

    @pyqtSlot()
    def reset(self):
        print("Reset")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    t = Test()
    t.show()
    sys.exit(app.exec_())