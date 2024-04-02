import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget, QLineEdit


def on_choose_file_1btn_click():
    print('Button 1 clicked!')
    # print(f"Key Pressed: {event.char}")
    # choose_file1 = username_entry.get()
    # entry_text = tk.StringVar()
    # entry = tk.Entry(root, textvariable=entry_text)
    # new_text = "Example text"
    # entry_text.set(new_text)
    # entry_text.set(fd.askopenfilename())

    # choose_file1 = fd.askopenfilename()
    # file1path.
def on_choose_file_2btn_click():
    print('Button 2 clicked!')

# def handle_choose_file2():
    # print(f"Key Pressed: {event.char}")
    # fd.askopenfilename()


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("File paths")
# Add widgets

# file1
# file1Lbl = tk.Label(window, text="File 1 path")
# file1Lbl.grid(row=0, column=0)
layout = QGridLayout()
label1 = QLabel("File 1 path")
layout.addWidget(label1, 0, 0)
# file1path = tk.Entry(window)]
# entry_text = tk.StringVar()
# file1path = tk.Entry(window, textvariable=entry_text)
# root, textvariable=entry_text
# file1path.grid(row=0, column=1)
# choose_file_1btn = tk.Button(window, text="file 1", command=handle_choose_file1)
# choose_file_1btn.grid(row=0, column=2)
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

# file2
# file2Lbl = tk.Label(window, text="File 2 path")
# file2Lbl.grid(row=1, column=0)
# file1path = tk.Entry(window)
# file1path.grid(row=1, column=1)
# choose_file_2btn = tk.Button(window, text="file 2", command=handle_choose_file2)
# choose_file_2btn.grid(row=1, column=2)


# Start the event loop
window.setLayout(layout)
window.show()
sys.exit(app.exec())
