import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont("Times",14)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Text Editor")
        self.setGeometry(250,150,500,500)
        self.UI()
        

    def UI(self):
       # for multiple lines
       self.editor=QTextEdit(self)
       self.editor.move(150,80)
       self.editor.setAcceptRichText(False) # to accept rich text
       button=QPushButton("Send",self)
       button.move(330,280)
       button.clicked.connect(self.getValue)
       
       self.show()

    def getValue(self):
        text=self.editor.toPlainText() # for different text styles
        print(text)
    
    
def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())


if __name__=='__main__':
    main()