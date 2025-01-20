import sys
from PyQt5 import QtWidgets, QtCore

import mainui
import convet_field_qt_manager
    
class App(QtWidgets.QMainWindow, mainui.Ui_MainWindow, convet_field_qt_manager.ConveyFieldQtManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
frame = App()

frame.initializeField(16, 16)
frame.initializeManger()
frame.initializeGameFieldFillButtons()
frame.changeAllButtons(0)

frame.show()

app.exec()

