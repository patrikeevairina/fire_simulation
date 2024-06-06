from dialog_ui import Ui_SettingsDialog
from PySide6.QtCore import Signal, Slot

from PySide6.QtWidgets import QDialog

class SettingsDialog(QDialog):
    new_field_signal = Signal(float)
    new_simulation_signal = Signal(float, float)

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.treeFactor = self.ui.treeFactorBox.value()

        self.finished.connect(self.on_accept_dialog)
    

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