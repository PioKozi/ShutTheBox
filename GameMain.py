from PyQt5 import QtGui, QtWidgets, QtCore, QtTest, uic
import random
from pathlib import Path
import sys

class Game(QtWidgets.QWidget):
    """docstring for Game."""
    def __init__(self):
        super(Game, self).__init__()
        uic.loadUi("GameMain.ui", self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    gameW = Game()
    gameW.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
