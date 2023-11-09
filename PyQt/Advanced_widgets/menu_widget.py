import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore  import Qt
from PyQt5.QtGui  import QFont

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Widget")
        self.setGeometry(350,150,600,600)
        self.UI()

    def UI(self):
        ##############Main Menu###############3
        menubar=self.menuBar()
        file=menubar.addMenu("File")
        edit=menubar.addMenu("Edit")
        code=menubar.addMenu("Code")
        help_=menubar.addMenu("Help")

        ##############Sub Menu items###########
        new=QAction("New Project", self)
        new.setShortcut("Ctrl+0")
        file.addAction(new)
        open=QAction("Open", self)
        open.setShortcut("Ctrl+1")
        file.addAction(open)
        exit=QAction("Exit", self)
        file.addAction(exit)
        exit.setShortcut("Ctrl+2")
        #######################################
        


        self.show()

def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()