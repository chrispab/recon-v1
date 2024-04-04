import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QGridLayout,
    QWidget,
    QLineEdit,
)

from PyQt6.uic import loadUi


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Load the UI file
        loadUi("src/5_simple_gui.ui", self)


if __name__ == "__ main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

app = QApplication([])
window = MyWindow()
window.show()
app.exec()
