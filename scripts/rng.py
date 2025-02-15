import random
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt

# Potential future adds: Rolling results history?

class RNG(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Number Generator")

        self.ceilingLabel = QLabel("Set ceiling:")
        self.ceilingInput = QLineEdit()
        self.ceilingInput.setValidator(QIntValidator())
        self.ceilingInput.setPlaceholderText("Max")
        self.ceilingInput.setFixedWidth(120)

        self.resultLabel = QLabel("Result:")
        self.resultOutput = QLineEdit()
        self.resultOutput.setReadOnly(True)
        self.resultOutput.setFixedWidth(120)

        self.button = QPushButton("Roll")
        self.button.setFixedSize(80, 30)
        self.button.clicked.connect(self.rollForRNG)

        # Configure layout
        layout = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()

        row1.setSpacing(10)
        row2.setSpacing(10)

        row1.addStretch()
        row1.addWidget(self.ceilingLabel)
        row1.addWidget(self.ceilingInput)
        row1.addStretch()

        row2.addStretch()
        row2.addWidget(self.resultLabel)
        row2.addWidget(self.resultOutput)
        row2.addStretch()

        row1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        row2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Parent layout
        layout.addSpacing(20)
        layout.addLayout(row1)
        layout.addSpacing(10)
        layout.addLayout(row2)
        layout.addSpacing(10)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
        # Apply layout
        self.setLayout(layout)


    def rollForRNG(self):
        try:
            value = self.ceilingInput.text()
            if value:
                result = random.randint(1, int(value))
                self.resultOutput.setText(str(result))
            else:
                self.resultOutput.setText("Enter a number")
        except ValueError:
            self.resultOutput.setText("Try again")