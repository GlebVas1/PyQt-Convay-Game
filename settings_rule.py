
import rules as ru
import copy

from PyQt5 import QtWidgets, QtCore, QtGui
from rule import Rule

class SettingsRuleManager(object):
    """Interface used for realtime resetting in-game rules"""

    thisRule = Rule()

    settingsRuleCheckBoxesSurvive = []
    settingsRuleCheckBoxesArrive = []

    def settingsRuleInitializeActions(self):
        self.ruleLoadbutton.clicked.connect(self.settingsRuleLoadPreset)
        self.ruleApply.clicked.connect(self.settingsRuleApplyRule)
        self.ruleSave.clicked.connect(self.settingsRuleSaveRule)
        # self.ruleComboBox.currentIndexChanged.connect(self.loadPreset)

    def settingsRuleInitializeFrame(self):
        """Initialize frame with rule neighbor checkboxes"""

        for i in range(9):
            checkbox = QtWidgets.QCheckBox(self.ruleCheckFrame)
            checkbox.setObjectName("RuleArriveCB" + str(i))
            checkbox.setGeometry(QtCore.QRect(10 + 40 * i, 40, 20, 20))
            checkbox.setText("")
            self.settingsRuleCheckBoxesArrive.append(checkbox)
            ru.loadRulesFromFile()

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
        """Initializes rule combobox"""
        for name, pallete in ru.rulesDict.items():
            self.ruleComboBox.addItem(name)

    def settingsRuleInitializeManager(self, rule : Rule):
        """Just makes self.thisRule and self.calc.this rule the same"""
        self.thisRule = copy.copy(rule)
        self.calc.thisRule = self.thisRule

    def settingsRuleMakePreview(self, rule : Rule):
        """Make a preview for the selected rule"""
        for i in range(9):
            self.settingsRuleCheckBoxesArrive[i].setChecked(rule.arriveIfNeighborCount[i] == 1)
            self.settingsRuleCheckBoxesSurvive[i].setChecked(rule.surviveIfNeighborCount[i] == 1)
        self.ruleGenerationsSpinBox.setValue(rule.generationsCount + 1)
        self.ruleName.setText(self.ruleComboBox.currentText())

    def settingsRuleLoadPreset(self):
        """Load a preset from checkbox and push it to the preview frame"""
        name = self.ruleComboBox.currentText()
        rule = copy.copy(ru.rulesDict[name])
        self.ruleName.setText(self.ruleComboBox.currentText())
        self.settingsRuleMakePreview(rule)

    def settingsRuleSaveRule(self):
        """Save applied(!) rule to preview"""
        if self.ruleName.toPlainText() not in ru.rulesDict.keys():
            self.ruleComboBox.addItem(self.ruleName.toPlainText())
        
        ru.rulesDict[self.ruleName.toPlainText()] = copy.deepcopy(self.thisRule)
        self.settingsRuleSaveToFile()

    def settingsRuleSaveToFile(self):
        ru.saveToFile()
        
    def settingsRuleApplyRule(self):
        """Apply fule to the game"""
        for i in range(9):
            self.thisRule.arriveIfNeighborCount[i] = 1 if self.settingsRuleCheckBoxesArrive[i].isChecked() else 0
            self.thisRule.surviveIfNeighborCount[i] = 1 if self.settingsRuleCheckBoxesSurvive[i].isChecked() else 0

        self.thisRule.generationsCount = self.ruleGenerationsSpinBox.value() - 1

        self.calc.initializeStatistics() # need to update/reintialize satistics dictionary to match current genrations count

        self.calc.applyRuleGenerationChanges() # need to rebuild ingame field with new new rule generations threshold
        
        self.conveyFieldQtManagerSyncChanges() # need to synchronize rule changes
