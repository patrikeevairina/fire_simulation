from form_ui import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal, Slot, QTimer
import time

from func_kernel import *

class MainWindow(QMainWindow):
    request_settings_dialog = Signal()

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.settingsTBtn.clicked.connect(self.req_settings)
        self.ui.startSimulationTBtn.clicked.connect(self.start_timer)
        self.ui.stopSimulationTBtn.clicked.connect(self.stop_timer)
        self.ui.field.fill()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.new_tree_factor = 0.05
        self.fire_factor = 0.001


    @Slot()
    def hand_simulate_step(self):
        self.ui.field.updateCells(interface(self.ui.field.cellStateList(), self.ui.field.columnCount(), self.ui.field.rowCount(), self.new_tree_factor,  self.fire_factor))


    @Slot()
    def start_timer(self):
        self.timer.start(200)

    @Slot()
    def stop_timer(self):
        self.timer.stop()

    @Slot()
    def update(self):
        interval = time.time()
        new_cells = interface(self.ui.field.cellStateList(), self.ui.field.columnCount(), self.ui.field.rowCount(), self.new_tree_factor,  self.fire_factor)
        # print("update {}".format(time.time() - interval))
        self.ui.statusBar.showMessage("последнее обновление данных заняло {:.2f} мс".format(((time.time() - interval) * 1000)))
        interval = time.time()
        self.ui.field.updateCells(new_cells)
        # print("redraw {}".format(time.time() - interval))

    @Slot()
    def req_settings(self):
        print("request settings dialog window")
        self.request_settings_dialog.emit()


    @Slot(float, float, float)
    def new_field_settings(self, treeFillFactor):
        self.ui.field.fill(treeFillFactor)
        print("update field")

    
    @Slot(float, float)
    def new_simulation_settings(self, randomFireFactor, newTreeFactor):
        self.new_tree_factor = newTreeFactor
        self.fire_factor = randomFireFactor
        print("new simulation settings")
