import random
from PyQt6.QtWidgets import QWidget, QTextEdit, QLabel, QVBoxLayout, QPushButton, QGroupBox
from PyQt6.QtCore import Qt

# Potential future adds:
# Add I/O for drawing lists from files

class RNGList(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random List Selector")

        self.selectList = ["Option A", "Option B", "Option C", "Option D"]

        # Input Section
        input_group = QGroupBox("Input List")
        input_layout = QVBoxLayout()

        self.instructionsLabel = QLabel("Enter all list items (comma or return delimited):")
        self.listInput = QTextEdit()
        self.listInput.setPlaceholderText("Item 1, Item 2, Item 3")

        self.setListButton = QPushButton("Set List")
        self.setListButton.setFixedSize(200, 30)
        self.setListButton.clicked.connect(self.updateList)

        self.currentListLabel = QLabel("Current List:")
        self.currentListDisplay = QTextEdit()
        self.currentListDisplay.setReadOnly(True)
        self.updateListDisplay()

        input_layout.setSpacing(10)
        input_layout.addWidget(self.instructionsLabel)
        input_layout.addWidget(self.listInput)
        input_layout.addWidget(self.setListButton, alignment=Qt.AlignmentFlag.AlignCenter)
        input_layout.addWidget(self.currentListLabel)
        input_layout.addWidget(self.currentListDisplay)
        input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_group.setLayout(input_layout)

        # Output Section
        output_group = QGroupBox("Result")
        output_layout = QVBoxLayout()

        self.rollButton = QPushButton("Retrieve From List")
        self.rollButton.setFixedSize(200, 30)
        self.rollButton.clicked.connect(self.rollForRNG)

        self.outputBox = QTextEdit()
        self.outputBox.setReadOnly(True)

        output_layout.setSpacing(10)
        output_layout.addWidget(self.rollButton, alignment=Qt.AlignmentFlag.AlignCenter)
        output_layout.addWidget(self.outputBox)
        output_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        output_group.setLayout(output_layout)

        # Parent Layout
        layout = QVBoxLayout()

        layout.addWidget(input_group)
        layout.addSpacing(10)
        layout.addWidget(output_group)

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Apply layout
        self.setLayout(layout)

    # Update selectList with options entered by the user
    def updateList(self):
        listText = self.listInput.toPlainText().strip()

        if not listText:
            return
        
        if "," in listText:
            items = [item.strip() for item in listText.split()]
        else:
            items = [item.strip() for item in listText.splitlines()]

        if items:
            self.selectList = items
            self.updateListDisplay()
            self.listInput.clear()

    def updateListDisplay(self):
        self.currentListDisplay.clear()
        listDisplay = "\n".join(self.selectList)
        self.currentListDisplay.setText(listDisplay)

    def rollForRNG(self):
        self.outputBox.setText(self.selectList[random.randint(0, len(self.selectList)-1)])