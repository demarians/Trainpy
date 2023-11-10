import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import sys
import sqlite3



con = sqlite3.connect('C:/Users/salva/Repositories/Trainpy/Projects/second_proj/employees.db')
cur=con.cursor()

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My employees app")
        self.setGeometry(450,150,750,800)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()  


    def mainDesign(self):
        self.employeeList=QListWidget()
        self.btnNew=QPushButton("New")
        self.btnUpdate=QPushButton("Update")
        self.btnDelete=QPushButton("Delete")


    def layouts(self):
        ###############Layouts################
        self.mainLayout=QHBoxLayout()
        self.leftLayout=QFormLayout()
        self.rightMainLayout=QVBoxLayout()
        self.rightTopLayout=QHBoxLayout()
        self.rightBottomLayout=QHBoxLayout()
        ######Adding child layouts to main layout###

        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        self.mainLayout.addLayout(self.leftLayout, 40)  # 40% o the mainLayout
        self.mainLayout.addLayout(self.rightMainLayout, 60) #60% of the mainLayout
        ######Adding widgets to layouts#########

        self.rightTopLayout.addWidget(self.employeeList)
        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnDelete)
        self.rightBottomLayout.addWidget(self.btnUpdate)

        ######Adding widgets to main Layout######

        self.setLayout(self.mainLayout)


def main():
    APP=QApplication(sys.argv)
    window=Main()
    sys.exit(APP.exec_())


if __name__=="__main__":
    main()
