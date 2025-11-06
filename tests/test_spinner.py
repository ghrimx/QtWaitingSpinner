import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt6.QtCore import QTimer


from pyqtspinner import WaitingSpinner
from pyqtspinner.configurator import SpinnerConfigurator


def test_spinner_creation(qtbot):
    parent = QWidget()
    spinner = WaitingSpinner(parent)

    spinner.start()
    spinner.stop()


def test_randomization_not_raising_value_errors(qtbot):
    configurator = SpinnerConfigurator()

    configurator._randomize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    spinner = WaitingSpinner(window)

    window.show()

    spinner.start()

    def stop():
        spinner.stop()

    QTimer.singleShot(5000, stop)
    
    sys.exit(app.exec())
