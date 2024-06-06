from dialog_ui import Ui_SettingsDialog
from simulation_settings_ui import Ui_Dialog
from PySide6.QtCore import Signal, Slot, Qt

from PySide6.QtWidgets import QDialog

class FieldSettings(QDialog):
    new_field_signal = Signal(float)
    new_simulation_signal = Signal(float, float)

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_SettingsDialog()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self)
        self.treeFactor = self.ui.treeFactorBox.value()
        self.ui.closePBtn.clicked.connect(self.close)
        self.accepted.connect(self.on_accept_dialog)
    

    @Slot()
    def on_req_settings_dialog(self):
        self.show() if self.isHidden() == True else self.hide()


    @Slot()
    def on_accept_dialog(self):
        randomFireFactor = self.ui.randomFireBox.value() / 100.0
        newTreeFactor = self.ui.newTreeBox.value() / 100.0
        self.new_simulation_signal.emit(randomFireFactor, newTreeFactor)
        
        if self.treeFactor == self.ui.treeFactorBox.value():
            return
        
        self.treeFactor = self.ui.treeFactorBox.value()
        treeFillFactor = (float)(self.ui.treeFactorBox.value()) / 100.0
        self.new_field_signal.emit(treeFillFactor)



class SimulationSettings(QDialog):
    new_timeout_signal = Signal(int)
    new_field_size_signal = Signal(int, int, int)

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.timer = 200
        self.field_width = 180
        self.field_height = 80
        self.cell = 15

        self.ui = Ui_Dialog()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.setupUi(self)
        self.ui.closePBtn.clicked.connect(self.close)
        self.accepted.connect(self.on_accept_dialog)

    @Slot()
    def on_req_settings_dialog(self):
        self.show() if self.isHidden() == True else self.hide()

    @Slot()
    def on_accept_dialog(self):
        if self.timer != self.ui.timerSBox.value():
            self.timer = self.ui.timerSBox.value()
            self.new_timeout_signal.emit(self.timer)

        if self.field_width != self.ui.widthSBox.value() \
        or self.field_height != self.ui.heightSBox.value() \
        or self.cell != self.ui.cellSBox.value():
            self.field_width = self.ui.widthSBox.value()
            self.field_height = self.ui.heightSBox.value()
            self.cell = self.ui.cellSBox.value()
            self.new_field_size_signal.emit(self.cell, self.field_width, self.field_height)
            # print(self.field_width, self.field_height, self.cell)