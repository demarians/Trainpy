import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore  import Qt
from PyQt5.QtGui  import QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Widget")
        self.setGeometry(350,150,600,500)
        self.UI()

    def UI(self):
        vbox=QVBoxLayout()
        self.table=QTableWidget()
        btn=QPushButton("Get")
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem("Surame"))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem("Adress"))
        # self.table.horizontalHeader().hide()
        # self.table.verticalHeader().hide()
        self.table.setItem(0,0,QTableWidgetItem("First Item"))
        # value= self.table.itemClicked()
        self.table.setItem(0,1,QTableWidgetItem("First Item"))
        self.table.setItem(1,2,QTableWidgetItem("First Item"))
        self.table.setItem(4,2,QTableWidgetItem("First Item"))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)    # to not be able to edit the content of a cell
        self.table.doubleClicked.connect(self.doubleClicked)
        btn.clicked.connect(self.getValue)
        vbox.addWidget(self.table)
        vbox.addWidget(btn)
        self.setLayout(vbox)

        self.show()

    def getValue(self):
        for item in self.table.selectedItems():
            print(item.text(),item.row(),item.column())

    def doubleClicked(self):
        for item in self.table.selectedItems():
            print(item.text(),item.row(),item.column())



def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()