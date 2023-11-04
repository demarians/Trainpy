import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using labels")
        self.setGeometry(50,50,350,350)
        self.UI()
        

    def UI(self):
       self.show()


def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())


if __name__=='__main__':
    main()