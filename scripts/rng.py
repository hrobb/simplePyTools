import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt

# Potential future adds: Rolling results history?

class RNG(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Number Generator")

        self.desc = QLabel("Set range for num:")
        self.desc.setContentsMargins(0, 25, 0, 0)
        self.inpBox = QLineEdit()
        self.inpBox.setValidator(QIntValidator())
        self.inpBox.setPlaceholderText("Max")
        self.desc2 = QLabel("Result:")
        self.inpBox2 = QLineEdit()
        self.inpBox2.setReadOnly(True)
        self.button = QPushButton("Roll")
        self.button.clicked.connect(self.rollForRNG)

        # Configure layout
        layout = QVBoxLayout()
        layout.addWidget(self.desc, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.inpBox, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.desc2, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.inpBox2, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
        # Apply layout
        self.setLayout(layout)


    def rollForRNG(self):
        try:
            value = self.inpBox.text()
            if value:
                result = random.randint(1, int(value))
                self.inpBox2.setText(str(result))
            else:
                self.inpBox2.setText("Enter a number")
        except ValueError:
            self.inpBox2.setText("Try again")