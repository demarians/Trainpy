import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import sys
import sqlite3
from PyQt5.QtGui import QPixmap,QFont



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
        self.btnNew.clicked.connect(self.addEmployee)
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


    def addEmployee(self):  # i create an instance of a class not yet defined
        self.newEmployee=AddEmployee()
        self.close()

class AddEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employees")
        self.setGeometry(450,150,350,600)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    def mainDesign(self):
        self.title=QLabel("Add Person")
        self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold') # also possible to change background background-color:red
        self.imgAdd=QLabel()
        self.imgAdd.setPixmap(QPixmap("C:/Users/salva/Repositories/Trainpy/Projects/second_proj/icons/person.png"))



    def layouts(self):
        ###########Creating main layouts###############
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout=QFormLayout()
        ###########Adding child layouts to main layouts#############3
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)

        ###########Adding widgets to layouts############
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgAdd)
        self.topLayout.addStretch()

        ###########Setting main layout for window################
        self.setLayout(self.mainLayout)


def main():
    APP=QApplication(sys.argv)
    window=Main()
    sys.exit(APP.exec_())


if __name__=="__main__":
    main()