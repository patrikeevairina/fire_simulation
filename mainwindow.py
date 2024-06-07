from form_ui import Ui_MainWindow
from enum_cell_type import WindType

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal, Slot, QTimer, Qt
import time

from func_kernel import *

class MainWindow(QMainWindow):
    request_settings_dialog = Signal()
    request_simulation_dialog = Signal()

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.closePBtn.clicked.connect(self.close)
        self.ui.minimizePBtn.clicked.connect(self.showMinimized)
        self.ui.maximizePBtn.clicked.connect(self.showMaximized)

        self.ui.editFieldTBtn.clicked.connect(self.request_settings_dialog.emit)
        self.ui.settingsTBtn.clicked.connect(self.request_simulation_dialog.emit)

        self.ui.startSimulationTBtn.clicked.connect(self.start_timer)
        self.ui.stepSimPBtn.clicked.connect(self.hand_simulate_step)
        self.ui.stopSimulationTBtn.clicked.connect(self.stop_timer)

        self.ui.field.fill()
        self.timer = QTimer()
        self.timeout = 200
        self.timer.timeout.connect(self.update)
        self.cell_width = 50
        self.field_width = 30
        self.field_height = 15
        self.is_clean = False

        self.tree_fill_factor = 0.8
        self.new_tree_factor = 0.0005
        self.fire_factor = 0.00001
        self.wind_factor = WindType.miss


    @Slot()
    def hand_simulate_step(self):
        interval = time.time()
        new_cells = interface(self.ui.field.cellStateList(), self.ui.field.columnCount(), self.ui.field.rowCount(), 
                              self.new_tree_factor, self.fire_factor, self.wind_factor, self.is_clean)
        update_text = "последнее обновление данных заняло {:.2f} мс ".format(((time.time() - interval) * 1000))
        self.ui.statusBar.showMessage(update_text)
        self.ui.field.updateCells(new_cells)


    @Slot()
    def start_timer(self):
        self.timer.start(self.timeout)


    @Slot()
    def stop_timer(self):
        self.timer.stop()


    @Slot()
    def update(self):
        interval = time.time()
        new_cells = interface(self.ui.field.cellStateList(), self.ui.field.columnCount(), self.ui.field.rowCount(), 
                              self.new_tree_factor, self.fire_factor, self.wind_factor, self.is_clean)
        # print("update {}".format(time.time() - interval))
        update_text = "последнее обновление данных заняло {:.2f} мс ".format(((time.time() - interval) * 1000))
        self.ui.statusBar.showMessage(update_text)
        # interval = time.time()
        self.ui.field.updateCells(new_cells)
        # redraw_text = "redraw {:.2f} мс".format(((time.time() - interval) * 1000))
        # self.ui.statusBar.showMessage(update_text + redraw_text)

    
    @Slot(int)
    def new_timer_timeout(self, new_timeout):
        self.timeout = new_timeout
        self.timer.setInterval(new_timeout)

    
    @Slot(int, int, int)
    def new_field_size_settings(self, cell, width, height):
        self.ui.field.fill(cell_width=cell, width=width, height=height, forest_fraction=self.tree_fill_factor)
        self.cell_width = cell
        self.field_width = width
        self.field_height = height


    @Slot(float, float, float)
    def new_field_settings(self, treeFillFactor):
        self.ui.field.fill(cell_width=self.cell_width, width=self.field_width, height=self.field_height, forest_fraction=treeFillFactor)
        self.tree_fill_factor = treeFillFactor

    
    @Slot(float, float, WindType)
    def new_simulation_factors(self, randomFireFactor, newTreeFactor, windFactor):
        self.new_tree_factor = newTreeFactor
        self.fire_factor = randomFireFactor
        self.wind_factor = windFactor

    
    @Slot(bool)
    def new_simulation_mode(self, is_clean):
        self.is_clean = is_clean