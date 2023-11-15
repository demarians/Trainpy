import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import sys,os
import sqlite3
from PyQt5.QtGui import QPixmap,QFont
from PIL import Image




con = sqlite3.connect('Trainpy/data/standardized_data/employees.db')
cur=con.cursor()
defaultImg="Trainpy/data/img/person.png"
person_id=None

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
        self.getEmployees()
        # self.displayFirstRecord()


    def mainDesign(self):
        self.setStyleSheet("font-size:14pt;font-family:Arial Bold;")
        self.employeeList=QListWidget()
        self.employeeList.itemClicked.connect(self.singleClicked)
        self.btnNew=QPushButton("New")
        self.btnNew.clicked.connect(self.addEmployee)
        self.btnUpdate=QPushButton("Update")
        self.btnUpdate.clicked.connect(self.updateEmployee)
        self.btnDelete=QPushButton("Delete")
        self.btnDelete.clicked.connect(self.deleteEmployee)


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

    def getEmployees(self):
        query="SELECT id,name,surname FROM employees" #not SELECT * coz not selecting all fields in the db
        employees=cur.execute(query).fetchall()
        for employee in employees:
            self.employeeList.addItem(str(employee[0])+"-"+employee[1]+" "+employee[2])

    # def displayFirstRecord(self): #only if there is an employee already in the database
    #     query="SELECT * FROM employees ORDER BY ROWid ASC LIMIT 1"
    #     employee=cur.execute(query).fetchone()
    #     # print(employee)
    #     img=QLabel()
    #     img.setPixmap(QPixmap("Trainpy/data/img"+employee[5]))
    #     name=QLabel(employee[1])
    #     surname=QLabel(employee[2])
    #     phone=QLabel(employee[3])
    #     email=QLabel(employee[4])
    #     address=QLabel(employee[6])
    #     self.leftLayout.setVerticalSpacing(20)
    #     self.leftLayout.addRow("",img)
    #     self.leftLayout.addRow("Name",name)
    #     self.leftLayout.addRow("Surname",surname)
    #     self.leftLayout.addRow("Phone",phone)
    #     self.leftLayout.addRow("Phone",email)
    #     self.leftLayout.addRow("Address",address)

    def singleClicked(self):
        for i in reversed(range(self.leftLayout.count())):
            widget=self.leftLayout.takeAt(i).widget()

            if widget is not None:
                widget.deleteLater()

        employe_e=self.employeeList.currentItem().text()
        id=employe_e.split("-")[0]
        query=("SELECT * FROM employees WHERE id=?")
        employee=cur.execute(query,(id,)).fetchone() # comma is necessary, single item tuple
        img=QLabel()
        img.setPixmap(QPixmap("Trainpy/data/img/"+employee[5]))
        name=QLabel(employee[1])
        surname=QLabel(employee[2])
        phone=QLabel(employee[3])
        email=QLabel(employee[4])
        address=QLabel(employee[6])
        self.leftLayout.setVerticalSpacing(20)
        self.leftLayout.addRow("",img)
        self.leftLayout.addRow("Name",name)
        self.leftLayout.addRow("Surname",surname)
        self.leftLayout.addRow("Phone",phone)
        self.leftLayout.addRow("Phone",email)
        self.leftLayout.addRow("Address",address)
 
    def deleteEmployee(self):
        if self.employeeList.selectedItems():
            person=self.employeeList.currentItem().text()
            # print(person)
            id =person.split("-")[0]
            mbox=QMessageBox.question(self,"Warning","Are you sure you want to delete this employee?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            if mbox==QMessageBox.Yes:
                try:
                    query="DELETE FROM employees WHERE id=?"
                    cur.execute(query,(id,))
                    con.commit()
                    QMessageBox.information(self,"Info!!","Person has been deleted")
                    self.close()
                    self.main=Main()

                except:
                    QMessageBox.information(self,"Warning!!","Person has not been deleted")
        else:
            QMessageBox.information(self,"Warning!!","Please select a person to delete")

    def updateEmployee(self):
        global person_id
        if self.employeeList.selectedItems():
            person=self.employeeList.currentItem().text()
            person_id=person.split("-")[0]
            # print(person_id)
            self.updateWindow=UpdateEmployee()
            self.close()

        else:
            QMessageBox.information(self,"Warning!!","Please select a person to update")            


class UpdateEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Employee")
        self.setGeometry(450,150,350,600)
        self.UI()
        self.show()

    def UI(self):
        self.getPerson()
        self.mainDesign()
        self.layouts()  

    def getPerson(self):
        global person_id
        query="SELECT * FROM employees WHERE id=?"
        employee=cur.execute(query,(person_id,)).fetchone()
        # print(employee)
        self.name=employee[1]
        self.surname=employee[2]
        self.phone=employee[3]
        self.email=employee[4]
        self.image=employee[5]
        self.address=employee[6]

    def closeEvent(self,event):
        self.main=Main()

    def mainDesign(self):
        self.setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
        #################Top Layout widgets###################
        self.title=QLabel("Update Person")
        self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold') # also possible to change background background-color:red
        self.imgAdd=QLabel()
        self.imgAdd.setPixmap(QPixmap("Trainpy/data/img/{}".format(self.image)))
        #################Bottom Layout widgets################
        self.nameLbl=QLabel("Name: ")
        self.nameEntry=QLineEdit()
        self.nameEntry.setText(self.name)
        self.surnameLbl=QLabel("Surname: ")
        self.surnameEntry=QLineEdit()
        self.surnameEntry.setText(self.surname)
        self.phoneLbl=QLabel("Phone: ")
        self.phoneEntry=QLineEdit()
        self.phoneEntry.setText(self.phone)
        self.emailLbl=QLabel("Email: ")
        self.emailEntry=QLineEdit()
        self.emailEntry.setText(self.email)
        self.imgLbl=QLabel("Picture: ")
        self.imgButton=QPushButton("Browse")
        self.imgButton.setStyleSheet("background-color:orange;font-size:10pt")
        self.imgButton.clicked.connect(self.uploadImg)
        self.addressLbl=QLabel("Address: ")
        self.addressEditor=QTextEdit()
        self.addressEditor.setText(self.address)
        self.addButton=QPushButton("Update")
        self.addButton.setStyleSheet("background-color:orange;font-size:10pt")
        self.addButton.clicked.connect(self.updateEmployee)



    def layouts(self):
        ###########Creating main layouts###############
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout=QFormLayout()
        ###########Adding child layouts to main layouts#############3
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)

        ###########Adding widgets to layouts############
                ##########top Layout###########
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgAdd)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(110,20,10,30)
                ##########bottom Layout###########
        self.bottomLayout.addRow(self.nameLbl,self.nameEntry)        
        self.bottomLayout.addRow(self.surnameLbl,self.surnameEntry)        
        self.bottomLayout.addRow(self.phoneLbl,self.phoneEntry)        
        self.bottomLayout.addRow(self.emailLbl,self.emailEntry)        
        self.bottomLayout.addRow(self.imgLbl,self.imgButton)        
        self.bottomLayout.addRow(self.addressLbl,self.addressEditor)   
        self.bottomLayout.addRow("",self.addButton)   

        ###########Setting main layout for window################
        self.setLayout(self.mainLayout) 

    def uploadImg(self):
        global defaultImg
        size=(128,128)  # width and heigth of the image
        self.fileName,ok=QFileDialog.getOpenFileName(self,'Upload Image','','Image Files (*.jpg *.png)')    
        if ok:
            # print(self.fileName) # this will give the entire directory path
            defaultImg=os.path.basename(self.fileName)
            # print(newName)  #this is the just name of the file
            img=Image.open(self.fileName)
            img=img.resize(size)
            img.save("Trainpy/data/img/{}".format(defaultImg))

    def updateEmployee(self):
        global defaultImg
        global person_id
        name=self.nameEntry.text()
        surname=self.surnameEntry.text()
        phone=self.phoneEntry.text()
        email=self.emailEntry.text()
        img=defaultImg
        address=self.addressEditor.toPlainText()
        if (name and surname and phone !=""): #if they are not empty
            try:
                query="UPDATE employees set name=?, surname=?, phone=?, email=?, image=?, address=? WHERE id=?"
                cur.execute(query,(name,surname,phone,email,img,address,person_id))
                con.commit()    #every time you change your database
                QMessageBox.information(self,"Success","Person has been updated to employees")
                # self.close()
                # self.main=Main()
            except:
                QMessageBox.information(self,"Warning","Person has not been updated to employees")
        else:
            QMessageBox.information(self,"Warning","Fields cannot be empty")

    def closeEvent(self, event):
        self.main=Main() # when i close my updateEmployee window, i open a new main window

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
        self.setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
        #################Top Layout widgets###################
        self.title=QLabel("Add Person")
        self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold') # also possible to change background background-color:red
        self.imgAdd=QLabel()
        self.imgAdd.setPixmap(QPixmap("Trainpy/data/img/person.png"))
        #################Bottom Layout widgets################
        self.nameLbl=QLabel("Name: ")
        self.nameEntry=QLineEdit()
        self.nameEntry.setPlaceholderText("Enter Employee Name")
        self.surnameLbl=QLabel("Surname: ")
        self.surnameEntry=QLineEdit()
        self.surnameEntry.setPlaceholderText("Enter Employee Surname")
        self.phoneLbl=QLabel("Phone: ")
        self.phoneEntry=QLineEdit()
        self.phoneEntry.setPlaceholderText("Enter Employee Phone Number")
        self.emailLbl=QLabel("Email: ")
        self.emailEntry=QLineEdit()
        self.emailEntry.setPlaceholderText("Enter Employee Email")
        self.imgLbl=QLabel("Picture: ")
        self.imgButton=QPushButton("Browse")
        self.imgButton.setStyleSheet("background-color:orange;font-size:10pt")
        self.imgButton.clicked.connect(self.uploadImg)
        self.addressLbl=QLabel("Address: ")
        self.addressEditor=QTextEdit()
        self.addButton=QPushButton("Add")
        self.addButton.setStyleSheet("background-color:orange;font-size:10pt")
        self.addButton.clicked.connect(self.addEmployee)



    def layouts(self):
        ###########Creating main layouts###############
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout=QFormLayout()
        ###########Adding child layouts to main layouts#############3
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)

        ###########Adding widgets to layouts############
                ##########top Layout###########
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgAdd)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(110,20,10,30)
                ##########bottom Layout###########
        self.bottomLayout.addRow(self.nameLbl,self.nameEntry)        
        self.bottomLayout.addRow(self.surnameLbl,self.surnameEntry)        
        self.bottomLayout.addRow(self.phoneLbl,self.phoneEntry)        
        self.bottomLayout.addRow(self.emailLbl,self.emailEntry)        
        self.bottomLayout.addRow(self.imgLbl,self.imgButton)        
        self.bottomLayout.addRow(self.addressLbl,self.addressEditor)   
        self.bottomLayout.addRow("",self.addButton)   

        ###########Setting main layout for window################
        self.setLayout(self.mainLayout)

    def uploadImg(self):
        global defaultImg
        size=(128,128)  # width and heigth of the image
        self.fileName,ok=QFileDialog.getOpenFileName(self,'Upload Image','','Image Files (*.jpg *.png)')    
        if ok:
            # print(self.fileName) # this will give the entire directory path
            defaultImg=os.path.basename(self.fileName)
            # print(newName)  #this is the just name of the file
            img=Image.open(self.fileName)
            img=img.resize(size)
            img.save("Trainpy/data/img/{}".format(defaultImg))

    def addEmployee(self):
        global defaultImg
        name=self.nameEntry.text()
        surname=self.surnameEntry.text()
        phone=self.phoneEntry.text()
        email=self.emailEntry.text()
        img=defaultImg
        address=self.addressEditor.toPlainText()
        if (name and surname and phone !=""): #if they are not empty
            try:
                query="INSERT INTO employees (name,surname,phone,email,image,address) VALUES(?,?,?,?,?,?)"
                cur.execute(query,(name,surname,phone,email,img,address))
                con.commit()    #every time you change your database
                QMessageBox.information(self,"Success","Person has been added to employees")
                # self.close()
                # self.main=Main()
            except:
                QMessageBox.information(self,"Warning","Person has not been added to employees")
        else:
            QMessageBox.information(self,"Warning","Fields cannot be empty")

    def closeEvent(self, event):
        self.main=Main() # when i close my addEmployee window, i open a new main window


def main():
    APP=QApplication(sys.argv)
    window=Main()
    sys.exit(APP.exec_())


if __name__=="__main__":
    main()
