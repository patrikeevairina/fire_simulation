from mainwindow import MainWindow
from settingsdialog import FieldSettings, SimulationSettings

from PySide6.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    settingsDialog = FieldSettings()
    simulationSettings = SimulationSettings()

    mainWindow.request_settings_dialog.connect(settingsDialog.on_req_settings_dialog)
    mainWindow.request_simulation_dialog.connect(simulationSettings.on_req_settings_dialog)

    settingsDialog.new_field_signal.connect(mainWindow.new_field_settings)
    settingsDialog.new_simulation_signal.connect(mainWindow.new_simulation_settings)
    
    simulationSettings.new_field_size_signal.connect(mainWindow.new_field_size_settings)
    simulationSettings.new_timeout_signal.connect(mainWindow.new_timer_timeout)

    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()