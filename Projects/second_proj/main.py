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
        self.layouts()  # sth wrong with the previous commit


    def mainDesign(self):
        pass

    def layouts(self):
        self.mainLayout=QHBoxLayout()
        self.leftLayout=QFormLayout()
        self.rightMainLayout=QVBoxLayout()
        self.rightTopLayout=QHBoxLayout()
        self.rightBottomLayout=QHBoxLayout()

        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.rightMainLayout)

        self.setLayout()


def main():
    APP=QApplication(sys.argv)
    window=main()
    sys.exit(APP.exec_())


if __name__=="__main__":
    main()
