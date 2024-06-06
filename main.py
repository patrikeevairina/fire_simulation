from mainwindow import MainWindow
from settingsdialog import SettingsDialog

from PySide6.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    settingsDialog = SettingsDialog()
    mainWindow.request_settings_dialog.connect(settingsDialog.on_req_settings_dialog)
    settingsDialog.new_field_signal.connect(mainWindow.new_field_settings)
    settingsDialog.new_simulation_signal.connect(mainWindow.new_simulation_settings)
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()