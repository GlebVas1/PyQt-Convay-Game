import sys
from PyQt5 import QtWidgets, QtCore
import mainui
import convet_field_qt_manager
import calc as cl

    
class App(QtWidgets.QMainWindow, mainui.Ui_MainWindow, convet_field_qt_manager.ConveyFieldQtManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
frame = App()
b
frame.InitializeField(9, 8)
frame.fillButtons()
frame.changeAllButtons(0)

frame.show()

app.exec()
