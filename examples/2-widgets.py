import sys
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QLineEdit,
    QCheckBox,
    QVBoxLayout,
    QWidget,
)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyQt Widgets")
layout = QVBoxLayout()
label = QLabel("Label Widget")
layout.addWidget(label)
button = QPushButton("Button Widget")
layout.addWidget(button)
entry = QLineEdit()
layout.addWidget(entry)
checkbox = QCheckBox("Checkbox Widget")
layout.addWidget(checkbox)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
