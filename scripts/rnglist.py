import random
from PyQt6.QtWidgets import QWidget, QTextEdit, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt

# Potential future adds:
# Add interface for altering the list 
# Add I/O for drawing lists from files

class RNGList(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random List Selector")
        
        self.button = QPushButton("Retrieve From List")
        self.button.setFixedSize(200, 30)
        self.button.clicked.connect(self.rollForRNG)

        self.outputLabel = QLabel("Result:")
        self.outputBox = QTextEdit()
        self.outputBox.setReadOnly(True)

        # Configure layout
        layout = QVBoxLayout()
        row1 = QVBoxLayout()

        row1.setSpacing(10)

        row1.addWidget(self.outputLabel)
        row1.addWidget(self.outputBox)
        row1.addStretch()

        row1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Parent Layout
        layout.addSpacing(20)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(10)
        layout.addLayout(row1)

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Apply layout
        self.setLayout(layout)


    def rollForRNG(self):
        selectList = ["Option A", "Option B", "Option C", "Option D"]
        self.outputBox.setText(selectList[random.randint(0, len(selectList)-1)])