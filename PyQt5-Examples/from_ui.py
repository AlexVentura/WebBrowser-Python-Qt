import sys

from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

w = uic.loadUi("main.ui")
w.setWindowTitle("Lexynux UI")
w.show()

sys.exit(app.exec_())