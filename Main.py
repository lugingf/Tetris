#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor

class Tetris(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        self.tboard.start()

        self.resize(180,380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):

        screen = QDescktopWidget().screenGeometry
        size = self.geometry
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

class Board(QFrame):

# Запуск-хуяпуск тетриса
if __name__ == '__main__':

    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())