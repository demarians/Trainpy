import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File dialogs")
        self.setGeometry(350,150,400,400)
        self.UI()

    def UI(self):
        self.gridLayout=QGridLayout()
        # btn1=QPushButton("Button 1")
        # btn2=QPushButton("Button 2")
        # btn3=QPushButton("Button 3")
        # btn4=QPushButton("Button 4")
        # self.gridLayout.addWidget(btn1,0,0)
        # self.gridLayout.addWidget(btn2,0,1)
        # self.gridLayout.addWidget(btn3,1,0)
        # self.gridLayout.addWidget(btn4,1,1)
        for i in range(0,3): #row
            for j in range(0,3): #column
                btn=QPushButton("Button {}{}".format(i,j))
                self.gridLayout.addWidget(btn,i,j)
                btn.clicked.connect(self.clickMe)
                pass


        self.setLayout(self.gridLayout)
        self.show()
        
    def clickMe(self):
        buttonID=self.sender().text()
        if buttonID=="Button 00":
            print("Button 00 was clicked")
        elif buttonID=="Button 01":
            print("Button 01 was clicked")
        elif buttonID=="Button 10":
            print("Button 00 was clicked")
        else:
            print("Other button was pressed")


def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()