class SettingsFieldSize(object):

    def SettingsFieldSizeInititalizeActions(self):
        self.fieldSizeUpdate.clicked.connect(self.settingsFieldSizeChacngeField)

    def settingsFieldSizeChacngeField(self):
        self.xFieldSize = self.fieldSizeX.value()
        self.yFieldSize = self.fieldSizeY.value()
        self.calc.reinitializeFieldWithNewSize(self.xFieldSize, self.yFieldSize)
        self.initializeGameFieldFillButtons()
        