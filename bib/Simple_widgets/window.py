import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, ):
        super().__init__()
        self.setGeometry(50,50,300,450) # location of my window (x,y) and size of my window (x,y)
        self.setWindowTitle("This is our window title")

        self.show()


App= QApplication(sys.argv)
window=Window()
sys.exit(App.exec_())


