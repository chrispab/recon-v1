import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyWidget(QWidget):
    def keyPressEvent(self, event):
        print(f"Key Pressed: {event.text()}")


app = QApplication(sys.argv)
window = MyWidget()
window.setWindowTitle("PyQt Event Handling")
window.show()
sys.exit(app.exec_())
