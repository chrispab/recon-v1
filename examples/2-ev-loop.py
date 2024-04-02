import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


def handle_button_click():
    label.setText("Button Clicked!")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyQt Event Loop")
layout = QVBoxLayout()
label = QLabel("Hello, PyQt!")
layout.addWidget(label)
button = QPushButton("Click Mel")
button.clicked.connect(handle_button_click)
layout.addWidget(button)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
