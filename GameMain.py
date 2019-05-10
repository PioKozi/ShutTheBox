from PyQt5 import QtGui, QtWidgets, QtCore, QtTest, uic
import random
from pathlib import Path
import sys

class Game(QtWidgets.QWidget):
    """docstring for Game."""
    switchStates = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}
    switchUpdates = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}
    d1 = 0
    d2 = 0
    firstPress = True
    def __init__(self):
        super(Game, self).__init__()
        uic.loadUi("GameMain.ui", self)
        self.rollConfirm.clicked.connect(self.rollDice)
        self.restartButton.clicked.connect(self.restart)
        self.switch1.clicked.connect(lambda: self.toggleSwitch(self.switch1, 1))
        self.switch2.clicked.connect(lambda: self.toggleSwitch(self.switch2, 2))
        self.switch3.clicked.connect(lambda: self.toggleSwitch(self.switch3, 3))
        self.switch4.clicked.connect(lambda: self.toggleSwitch(self.switch4, 4))
        self.switch5.clicked.connect(lambda: self.toggleSwitch(self.switch5, 5))
        self.switch6.clicked.connect(lambda: self.toggleSwitch(self.switch6, 6))
        self.switch7.clicked.connect(lambda: self.toggleSwitch(self.switch7, 7))
        self.switch8.clicked.connect(lambda: self.toggleSwitch(self.switch8, 8))
        self.switch9.clicked.connect(lambda: self.toggleSwitch(self.switch9, 9))

    def restart(self):
        self.switchStates = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}
        self.switchUpdates = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}
        self.firstPress = True
        self.d1 = 0
        self.d2 = 0
        self.die1Label.setPixmap(QtGui.QPixmap())
        self.die2Label.setPixmap(QtGui.QPixmap())
        self.rollConfirm.setText("Confirm and Roll")
        self.setStyleSheet("")
        switchArray = [self.switch1, self.switch2, self.switch3, self.switch4, self.switch5, self.switch6, self.switch7, self.switch8, self.switch9]
        for switch in switchArray:
            switch.setStyleSheet("background-color:rgb(138, 226, 52)")
        self.disableAll()

    def toggleSwitch(self, switch, switchNum):
        if self.switchUpdates[switchNum] == False:
            switch.setStyleSheet("background-color:rgb(252, 233, 79)")
            self.switchUpdates[switchNum] = True
        else:
            switch.setStyleSheet("background-color:rgb(138, 226, 52);")
            self.switchUpdates[switchNum] = False
        if all(value == True for value in self.switchUpdates.values()):
            self.rollConfirm.setText("YOU WIN!")
            self.setStyleSheet("background-color:rgb(196, 160, 0);")

    def rollDice(self):
        if self.switchUpdates != self.switchStates or self.firstPress:#and as long as the two don't look the same, this can run
            self.switchStates.update(self.switchUpdates)
            self.firstPress = False
            self.d1 = random.randint(1, 6)
            self.d2 = random.randint(1, 6)
            self.die1Label.setPixmap(QtGui.QPixmap(str(Path("DiceFaces/Dice" + str(self.d1) + ".png"))))
            self.die2Label.setPixmap(QtGui.QPixmap(str(Path("DiceFaces/Dice" + str(self.d2) + ".png"))))
            self.checkLegalMoves()

    def disableAll(self):
        switchArray = [self.switch1, self.switch2, self.switch3, self.switch4, self.switch5, self.switch6, self.switch7, self.switch8, self.switch9]
        for switch in switchArray:
            switch.setEnabled(False)

    def checkLegalMoves(self):
        self.disableAll()
        ##if (self.d1 == 1 or self.d2 == 1 or self.d1 + self.d2 == 1) and self.switchUpdates[1] == False:
        ##    self.switch1.setEnabled(True)
        switchArray = [self.switch1, self.switch2, self.switch3, self.switch4, self.switch5, self.switch6, self.switch7, self.switch8, self.switch9]
        for switch in switchArray:
            if(self.d1 == switchArray.index(switch)+1 or self.d2 == switchArray.index(switch)+1 or self.d1 + self.d2 == switchArray.index(switch)+1) and self.switchUpdates[switchArray.index(switch)+1] == False:
                switch.setEnabled(True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gameW = Game()
    gameW.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
