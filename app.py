import sys
from PyQt5 import QtWidgets

import mainui
import convey_field_qt_manager
    
class App(QtWidgets.QMainWindow, mainui.Ui_MainWindow, convey_field_qt_manager.ConveyFieldQtManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
frame = App()

frame.ConveyFieldQtManagerInitializeActions()
frame.ConveyFieldQtManagerInitializeManager(16, 16)


frame.show()

app.exec()

