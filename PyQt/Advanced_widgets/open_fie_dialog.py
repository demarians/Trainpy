import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File dialogs")
        self.setGeometry(350,150,400,400)
        self.UI()

    def UI(self):
        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        self.editor=QTextEdit()
        fileButton=QPushButton("Open File")
        fileButton.clicked.connect(self.openFile)

        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(fileButton)
        hbox.addStretch()

        self.setLayout(vbox)

        self.show()

    def openFile(self):
        url =QFileDialog.getOpenFileName(self,"Open a file", "", "All Files(*);;*txt;;*png")
        print(url)
        fileUrl=url[0]
        file=open(fileUrl,"r")
        content=file.read()
        self.editor.setText(content)


def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__=='__main__':
    main()