import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

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
        exit.setIcon(QIcon("Trainpy/PyQt/Advanced_widgets/icons/exit.png"))
        exit.triggered.connect(self.exitFunc)
        ###############Tool Bar#########################
        tb=self.addToolBar("My toolbar")
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)   # to set the name under the icon
        newTb=QAction(QIcon('Trainpy/PyQt/Advanced_widgets/icons/folder.png'),"New",self)
        tb.addAction(newTb)
        openTb=QAction(QIcon("Trainpy/PyQt/Advanced_widgets/icons/empty.png"),"Open",self)
        tb.addAction(openTb)
        saveTb=QAction(QIcon("C:/Users/salva/Repositories/Trainpy/PyQt/Advanced_widgets/icons/save.png"),"Save",self)
        tb.addAction(saveTb)
        exitTb=QAction(QIcon("C:/Users/salva/Repositories/Trainpy/PyQt/Advanced_widgets/icons/exit.png"),"Exit",self)
        exitTb.triggered.connect(self.exitFunc)
        tb.addAction(exitTb)
        tb.actionTriggered.connect(self.btnFunc)
        self.combo=QComboBox()
        self.combo.addItems(["Spiderman","Superman","Batman"])
        tb.addWidget(self.combo)
        self.show()

    def exitFunc(self):
        mbox=QMessageBox.information(self, "Warning", "Are you sure to exit?",QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if mbox==QMessageBox.Yes:
            sys.exit()

    def btnFunc(self,btn): # I pass btn parameter coz i need to know wich btn is clicked
        if btn.text()=="New":   # it is text() because you are passing an external parameter
            print("You clicked New button")
        elif btn.text()=="Open":
            print("You clicked Open button")
        else:
            print("You clicked Save button")


def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()