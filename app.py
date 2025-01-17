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

frame.initializeField(25, 25)
frame.initializeManger()
frame.fillButtons()
frame.changeAllButtons(0)

frame.show()

app.exec()

# from PyQt5 import QtCore, QtWidgets
# import pyqtgraph as pg
# import numpy as np


# class MyWidget(pg.GraphicsLayoutWidget):

#     def __init__(self, parent=None):
#         super().__init__(parent=parent)

#         self.mainLayout = QtWidgets.QVBoxLayout()
#         self.setLayout(self.mainLayout)

#         self.timer = QtCore.QTimer(self)
#         self.timer.setInterval(100) # in milliseconds
#         self.timer.start()
#         self.timer.timeout.connect(self.onNewData)

#         self.plotItem = self.addPlot(title="Lidar points")

#         self.plotDataItem = self.plotItem.plot([], pen=None, 
#             symbolBrush=(255,0,0), symbolSize=5, symbolPen=None)


#     def setData(self, x, y):
#         self.plotDataItem.setData(x, y)


#     def onNewData(self):
#         numPoints = 1000  
#         x = np.random.normal(size=numPoints)
#         y = np.random.normal(size=numPoints)
#         self.setData(x, y)


# def main():
#     app = QtWidgets.QApplication([])

#     pg.setConfigOptions(antialias=False) # True seems to work as well

#     win = MyWidget()
#     win.show()
#     win.resize(800,600) 
#     win.raise_()
#     app.exec_()

# main()