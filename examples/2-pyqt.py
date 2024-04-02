import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


def button_clicked():
    label.setText("Button Clicked!")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyQt Basics")
layout = QVBoxLayout()
label = QLabel("Hello, PyQt!")
layout.addWidget(label)
button = QPushButton("Click Me!")
button.clicked.connect(button_clicked)
layout.addWidget(button)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
