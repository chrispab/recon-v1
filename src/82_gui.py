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
        loadUi("src/82_gui.ui", self)
        # Connect button clicked signal to event handler
        self.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        # Get text from line edit
        text = self.lineEdit.text()
        # Update label text
        self.label. setText(f'Hello, {text}!')


if __name__ == "__ main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

app = QApplication([])
window = MyWindow()
window.show()
app.exec()
