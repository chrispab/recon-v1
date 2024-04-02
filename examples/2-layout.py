import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyQt Layouts")

layout = QGridLayout()
label1 = QLabel("Label 1")
layout.addWidget(label1, 0, 0)
label2 = QLabel("Label 2")
layout.addWidget(label2, 1, 0)
button = QPushButton("Button")
layout.addWidget(button, 0, 1, 2, 1)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
