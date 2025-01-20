from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont

class StopStartManager(object):

    gameStatePlayed = True

    def stopStartManagerInitializeActions(self):
        self.playButton.clicked.connect(self.stopStartManagerButtonAction)
        self.stopButton.clicked.connect(self.stopStartManagerButtonAction)
        self.playButton.setEnabled(False)

    def stopStartManagerButtonAction(self):
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