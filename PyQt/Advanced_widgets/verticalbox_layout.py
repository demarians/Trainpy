import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal Box Layout")
        self.setGeometry(350,150,400,400)
        self.UI()

    def UI(self):
        vbox=QVBoxLayout()
        button1=QPushButton("Save")
        button2=QPushButton("Exit")
        button3=QPushButton("Cancel")
        vbox.addStretch()
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        vbox.addStretch()
        self.setLayout(vbox)

        self.show()

    
def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()