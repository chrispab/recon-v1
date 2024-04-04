import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget, QLineEdit

from PyQt6.uic import loadUi



def on_choose_file_1btn_click():
    print('Button 1 clicked!')

def on_choose_file_2btn_click():
    print('Button 2 clicked!')


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("File paths")
# Add widgets

layout = QGridLayout()
label1 = QLabel("File 1 path")
layout.addWidget(label1, 0, 0)

label1 = QLabel("File 1 path")
layout.addWidget(label1, 0, 0)

file1path = QLineEdit()
layout.addWidget(file1path,0,1)

choose_file_1btn = QPushButton("file 1")
layout.addWidget(choose_file_1btn,0,2)
choose_file_1btn.clicked.connect(on_choose_file_1btn_click)

label2 = QLabel("File 2 path")
layout.addWidget(label2, 1, 0)

file2path = QLineEdit()
layout.addWidget(file2path,1,1)

choose_file_2btn = QPushButton("file 2")
layout.addWidget(choose_file_2btn,1,2)
choose_file_2btn.clicked.connect(on_choose_file_2btn_click)

# Start the event loop
window.setLayout(layout)
window.show()
sys.exit(app.exec())
