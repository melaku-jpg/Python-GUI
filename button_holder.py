from PySide6.QtWidgets import QMainWindow, QPushButton
class ButtonHolder(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Test app")
        button = QPushButton("Test")

    #Set up the button as our central widget
        self.setCentralWidget(button)