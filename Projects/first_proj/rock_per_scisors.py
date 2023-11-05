import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QPixmap

textFont=QFont("Times",14)
buttonFont=QFont("Arial",12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock, paper, scissors Game")
        self.setGeometry(350,150,500,500)
        self.UI()
        

    def UI(self):
       #############Scores###############
       self.scoreComputerText=QLabel("Computer Score: ", self)
       self.scoreComputerText.move(30,20)
       self.scoreComputerText.setFont(textFont)
       self.scorePlayer=QLabel("Your Score: ", self)
       self.scorePlayer.move(30,20)
       self.scorePlayer.setFont(textFont)
       #############Images###############
       self.imageComputer=QLabel(self)
       self.imageComputer.setPixmap(QPixmap("images/rock.png"))
       self.imageComputer.move(50,100)
       self.imagePlayer=QLabel(self)
       self.imagePlayer.setPixmap(QPixmap("images/rock.png"))
       self.imagePlayer.move(330,100)
       self.imageGame=QLabel(self)
       self.imageGame.setPixmap(QPixmap("images/game.png"))
       self.imageGame.move(230,160)

    
       self.show()



    
def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())


if __name__=='__main__':
    main()