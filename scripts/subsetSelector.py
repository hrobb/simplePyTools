import random
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt

# Potential future adds: 
# Add optional floor 

class SubsetSelector(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Subset Selector")

        self.ceilingLabel = QLabel("Set ceiling:")
        self.ceilingInput = QLineEdit()
        self.ceilingInput.setValidator(QIntValidator())
        self.ceilingInput.setPlaceholderText("Max")
        self.ceilingInput.setFixedWidth(120)

        self.amountLabel = QLabel("Amount to return:")
        self.amountInput = QLineEdit()
        self.amountInput.setValidator(QIntValidator())
        self.amountInput.setPlaceholderText("Amount")
        self.amountInput.setFixedWidth(120)

        self.button = QPushButton("Roll")
        self.button.setFixedSize(80, 30)
        self.button.clicked.connect(self.rollForSubset)

        self.resultLabel = QLabel("Result:")
        self.resultOutput = QTextEdit()
        self.resultOutput.setReadOnly(True)

        # Configure component layouts
        layout = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QVBoxLayout()

        row1.setSpacing(10)
        row2.setSpacing(10)
        row3.setSpacing(10)

        row1.addStretch()
        row1.addWidget(self.ceilingLabel)
        row1.addWidget(self.ceilingInput)
        row1.addStretch()

        row2.addStretch()
        row2.addWidget(self.amountLabel)
        row2.addWidget(self.amountInput)
        row2.addStretch()

        row3.addWidget(self.resultLabel)
        row3.addWidget(self.resultOutput)
        row3.addStretch()

        row1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        row2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        row3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Parent layout
        layout.addSpacing(20)
        layout.addLayout(row1)
        layout.addSpacing(10)
        layout.addLayout(row2)
        layout.addSpacing(10)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(10)
        layout.addLayout(row3)
        

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            
        # Apply layout
        self.setLayout(layout)

    def rollForSubset(self):
        rangeTotal = self.ceilingInput.text()
        resultNumber = self.amountInput.text()
        
        if not rangeTotal or not resultNumber:
            self.resultOutput.setText("Ensure all fields are populated")
            return
        
        try:
            ceiling = int(rangeTotal)
            resNumber = int(resultNumber)

            if ceiling < 1:
                self.resultOutput.setText("Ceiling must be at least 1")
                return
            
            if resNumber < 1:
                self.resultOutput.setText("Amount must be at least 1")
                return
            
            if resNumber > ceiling:
                self.resultOutput.setText("Amount can't be more than ceiling")
                return
            

            resultSet = random.sample(range(1, ceiling + 1), resNumber)
            resultSet.sort()
            self.resultOutput.setText(str(resultSet))

        except ValueError:
            self.resultOutput.setText("Invalid input")