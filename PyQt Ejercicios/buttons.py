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
        
# very important if you want to use a parameter in another
# function as text you need to create a self.parameter
    def UI(self):
        self.text=QLabel("My Text", self)
        enterButton=QPushButton("Enter",self)
        exitButton=QPushButton("Exit",self)
        self.text.move(160,50)
        enterButton.move(100,80)
        exitButton.move(200,80)
        enterButton.clicked.connect(self.enterFunc) #to create a functionality to the button
        exitButton.clicked.connect(self.exitFunc) #to create a functionality to the button
        self.show()

    def enterFunc(self):
        self.text.setText("You clicked Enter") # if you have a variable text too short to update
        # you need then to reset the length of it
        self.text.resize(150,20)
    def exitFunc(self):
        self.text.setText("You clicked Exit")
        self.text.resize(150,20)


def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())


if __name__=='__main__':
    main()