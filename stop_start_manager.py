from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont

class StopStartManager(object):

    gameStatePlayed = True

    def initializeStopStartManager(self):
        self.playButton.clicked.connect(self.gameStartStopButtonAction)
        self.stopButton.clicked.connect(self.gameStartStopButtonAction)
        self.playButton.setEnabled(False)

    def gameStartStopButtonAction(self):
        if self.gameStatePlayed:
            self.gameStatePlayed = False
            self.stopButton.setEnabled(False)
            self.playButton.setEnabled(True)
            self.updateTimer.stop()
        else:
            self.gameStatePlayed = True
            self.playButton.setEnabled(False)
            self.stopButton.setEnabled(True)
            self.updateTimer.start()