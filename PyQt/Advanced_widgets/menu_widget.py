import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

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
        ###############Set icons########################
        exit.setIcon(QIcon("Trainpy/PyQt/Advanced_widgets/items/exit.png"))
        exit.triggered.connect(self.exitFunc)

        self.show()

    def exitFunc(self):
        mbox=QMessageBox.information(self, "Warning", "Are you sure to exit?",QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if mbox==QMessageBox.Yes:
            sys.exit()

def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()