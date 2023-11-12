import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont("Times",16)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Spin boxes")
        self.setGeometry(250,150,500,500)
        self.UI()
        

    def UI(self):
       self.spinbox=QSpinBox(self)
       self.spinbox.move(150,100)
       self.spinbox.setFont(font)
       # to improve the range
       # self.spinbox.setMinimum(25)
       # self.spinbox.setMaximum(1000)
       self.spinbox.setRange(25,110)
       # self.spinbox.setPrefix("$ ")
       self.spinbox.setSuffix(" cm")
       # to increase value 5 multiple
       self.spinbox.setSingleStep(5)
       # self.spinbox.valueChanged.connect(self.getValue)
       button=QPushButton("Send", self)
       button.move(150,140)
       button.clicked.connect(self.getValue)
       self.show()

    def getValue(self):
        value=self.spinbox.value()
        print(value)
    
    
def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())


if __name__=='__main__':
    main()