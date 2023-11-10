import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import sys

from PyQt5.QtWidgets import QWidget


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My employees app")
        self.setGeometry(450,150,750,800)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()


    def mainDesign(self):
        pass


def main():
    APP=QApplication(sys.argv)
    window=main()
    sys.exit(APP.exec_())


if __name__=="__main__":
    main()
