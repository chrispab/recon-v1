
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from PyQt6.uic import loadUi


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Load the UI file
        loadUi("src/85_gui.ui", self)

    def on_pushButton_clicked(self):
        self.label.setText('Buttonkkkk Clicked!')


if __name__ == "__ main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

app = QApplication([])
window = MyWindow()
window.show()
app.exec()
