import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtCore import QTimer
from random import randint

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
       self.scorePlayer.move(300,20)
       self.scorePlayer.setFont(textFont)
       #############Images###############
       self.imageComputer=QLabel(self)
       self.imageComputer.setPixmap(QPixmap("C:/Users/salva/Repositories/Trainpy/Projects/first_proj/images/rock.png"))
       self.imageComputer.move(50,100)
       self.imagePlayer=QLabel(self)
       self.imagePlayer.setPixmap(QPixmap("C:/Users/salva/Repositories/Trainpy/Projects/first_proj/images/rock.png"))
       self.imagePlayer.move(330,100)
       self.imageGame=QLabel(self)
       self.imageGame.setPixmap(QPixmap("C:/Users/salva/Repositories/Trainpy/Projects/first_proj/images/game.png"))
       self.imageGame.move(230,160)
       #############Buttons################
       btnStart=QPushButton("Start",self)
       btnStop=QPushButton("Stop",self)
       btnStart.move(130,250)
       btnStop.move(280, 250)
       btnStart.clicked.connect(self.start)
       btnStop.clicked.connect(self.stop)
       self.timer=QTimer(self)
       self.timer.setInterval(100)
       self.timer.timeout.connect(self.playGame)

        
       self.show()

    
    def playGame(self):
        self.rndComputer=randint(1,3)
        if self.rndComputer == 1:
            self.imageComputer.setPixmap(QPixmap("C:/Users/salva/Repositories/Trainpy/Projects/first_proj/images/rock.png"))
        elif self.rndComputer == 2:
            self.imageComputer.setPixmap(QPixmap("C:/Users/salva/Repositories/Trainpy/Projects/first_proj/images/paper.png"))
        else:
            self.imageComputer.setPixmap(QPixmap("C:/Users/salva/Repositories/Trainpy/Projects/first_proj/images/scissors.png"))
        self.rndPlayer=randint(1,3)
        if self.rndPlayer == 1:
            self.imagePlayer.setPixmap(QPixmap("C:/Users/salva/Repositories/Trainpy/Projects/first_proj/images/rock.png"))
        elif self.rndPlayer == 2:
            self.imagePlayer.setPixmap(QPixmap("C:/Users/salva/Repositories/Trainpy/Projects/first_proj/images/paper.png"))
        else:
            self.imagePlayer.setPixmap(QPixmap("C:/Users/salva/Repositories/Trainpy/Projects/first_proj/images/scissors.png"))


    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()


    
def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())


if __name__=='__main__':
    main()