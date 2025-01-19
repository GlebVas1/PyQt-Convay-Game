from math import sqrt
import random
from PyQt5 import QtWidgets, QtCore, QtGui
from functools import partial

from rule import Rule

import rules as ru

import copy

class settingsRuleManager(object):

    thisRule = Rule()

    settingsRuleCheckBoxesSurvive = []
    settingsRuleCheckBoxesArrive = []

    def settingsRuleInitializeActions(self):
        self.ruleLoadbutton.clicked.connect(self.settingsRuleLoadPreset)
        self.ruleApply.clicked.connect(self.settingsRuleApplyRule)
        # self.ruleComboBox.currentIndexChanged.connect(self.loadPreset)

    def settingsRuleInitializeFrame(self):
        for i in range(9):
            checkbox = QtWidgets.QCheckBox(self.ruleCheckFrame)
            checkbox.setObjectName("RuleArriveCB" + str(i))
            checkbox.setGeometry(QtCore.QRect(10 + 40 * i, 40, 20, 20))
            checkbox.setText("")
            self.settingsRuleCheckBoxesArrive.append(checkbox)

        for i in range(9):
            checkbox = QtWidgets.QCheckBox(self.ruleCheckFrame)
            checkbox.setObjectName("RuleArriveCB" + str(i))
            checkbox.setGeometry(QtCore.QRect(10 + 40 * i, 80, 20, 20))
            checkbox.setText("")
            
            self.settingsRuleCheckBoxesSurvive.append(checkbox)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        for i in range(9):
            label = QtWidgets.QLabel(self.ruleCheckFrame)
            label.setObjectName("RuleLabel" + str(i))
            label.setText(str(i))
            label.setFont(font)
            label.setGeometry(QtCore.QRect(12 + 40 * i, 10, 20, 20))

    def settingsRuleInitializeComboBox(self):
        for name, pallete in ru.rulesDict.items():
            self.ruleComboBox.addItem(name)

    def settingsRuleInitializeManager(self, rule : Rule):
        self.thisRule = copy.copy(rule)
        self.calc.thisRule = self.thisRule

    def settingsRuleMakePreview(self, rule : Rule):
        for i in range(9):
            self.settingsRuleCheckBoxesArrive[i].setChecked(rule.arriveIfNeighborCount[i] == 1)
            self.settingsRuleCheckBoxesSurvive[i].setChecked(rule.surviveIfNeighborCount[i] == 1)
        self.ruleGenerationsSpinBox.setValue(rule.generationsCount + 1)

    def settingsRuleLoadPreset(self):
        name = self.ruleComboBox.currentText()
        rule = copy.copy(ru.rulesDict[name])
        self.settingsRuleMakePreview(rule)

    def settingsRuleApplyRule(self):
        for i in range(9):
            self.thisRule.arriveIfNeighborCount[i] = 1 if self.settingsRuleCheckBoxesArrive[i].isChecked() else 0
            self.thisRule.surviveIfNeighborCount[i] = 1 if self.settingsRuleCheckBoxesSurvive[i].isChecked() else 0

        self.thisRule.generationsCount = self.ruleGenerationsSpinBox.value() - 1

        self.calc.initializeStatistics()

        self.gameManagerSyncChanges()
