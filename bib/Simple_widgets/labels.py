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
       text1=QLabel("Hello Python",self)
       text2=QLabel("Hello Python",self)
       text1.move(100,50)
       text1.move(200,50)
       self.show()


def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())


if __name__=='__main__':
    main()