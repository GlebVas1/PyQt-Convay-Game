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

frame.InitializeField(9, 8)
frame.fillButtons()
frame.changeAllButtons(0)
c
frame.show()

# frame.changeAllButtons(0)
app.exec()

# class A(object):
#     def setup(self):
#         self.c = 156

# class C(object):
#     def __init__(self):
#         self.d = 345

# class B(A, C):
#     def __init__(self):
#         super().__init__()

# b = B()
# b.setup()
# print(b.d)

# class A:
#     def __init__(self):
#         self.b = 1
    
#     def change(self):
#         self.b = 2


# l = []

# for i in range(3):
#     a = A()
#     l.append(a)

# for i in range(3):
#     l[i].change()

# for i in range(3):
#     print(l[i].b)


# for i in l:
#     i.change()

# for i in range(3):
#     print(l[i].b)
