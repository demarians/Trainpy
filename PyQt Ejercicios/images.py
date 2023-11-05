import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using LineEdits")
        self.setGeometry(50,50,350,350)
        self.UI()
        

    def UI(self):
       self.image
        
       self.show()


    def getValues(self):
        name=self.nameTextBox.text()
        password=self.passTextBox.text()
        self.setWindowTitle("Your name is: " + name+"Your password is: " + password)


def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())


if __name__=='__main__':
    main()