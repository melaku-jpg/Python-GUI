#importing components we need
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton
from button_holder import ButtonHolder
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder")
        button = QPushButton("Click Me")

        #Set up the button as our central widget
        self.setCentralWidget(button)
app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()