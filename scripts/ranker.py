from PyQt6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt

# Potential future adds:

class ListRanker(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("List Ranker")

        self.rankedList = ["Option A", "Option B", "Option C", "Option D"]

        self.sorted_index = 1
        self.compare_index = 0
        self.current_item = None

        # Input Section
        input_group = QGroupBox("Input List")
        input_layout = QVBoxLayout()

        self.instructionsLabel = QLabel("Enter all list items (comma or return delimited):")
        self.listInput = QTextEdit()
        self.listInput.setPlaceholderText("Item 1, Item 2, Item 3")

        self.setListButton = QPushButton("Set List")
        self.setListButton.setFixedSize(200, 30)
        self.setListButton.clicked.connect(self.updateList)

        input_layout.setSpacing(10)
        input_layout.addWidget(self.instructionsLabel)
        input_layout.addWidget(self.listInput)
        input_layout.addWidget(self.setListButton, alignment=Qt.AlignmentFlag.AlignCenter)
        input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_group.setLayout(input_layout)

        # Output Section
        output_group = QGroupBox("Ranker and Output")
        output_layout = QVBoxLayout()

        ranking_section = QWidget()
        ranking_layout = QHBoxLayout()
        self.optionOneButton = QPushButton("Option 1", ranking_section)
        self.optionOneButton.setEnabled(False)
        self.optionOneButton.setFixedSize(200, 50)
        self.optionOneButton.clicked.connect(lambda: self.handleChoice(0))
        self.optionTwoButton = QPushButton("Option 2", ranking_section)
        self.optionTwoButton.setEnabled(False)
        self.optionTwoButton.setFixedSize(200, 50)
        self.optionTwoButton.clicked.connect(lambda: self.handleChoice(1))
        ranking_layout.addWidget(self.optionOneButton)
        ranking_layout.addWidget(self.optionTwoButton)
        ranking_section.setLayout(ranking_layout)

        self.outputBox = QTextEdit()
        self.outputBox.setReadOnly(True)

        output_layout.setSpacing(10)
        output_layout.addWidget(ranking_section)
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

    # Parse/accept input, if valid start sorting process
    def updateList(self):
        listText = self.listInput.toPlainText().strip()

        if not listText:
            return
        
        if "," in listText:
            items = [item.strip() for item in listText.split(',')]
        else:
            items = [item.strip() for item in listText.splitlines()]

        if items and len(items) >= 2:
            self.rankedList = items
            self.updateOutputDisplay()
            self.listInput.clear()

            self.sort()
        else:
            self.outputBox.setText("Please enter at least two items")
            return            

    def updateOutputDisplay(self):
        self.outputBox.clear()
        listDisplay = "\n".join(self.rankedList)
        self.outputBox.setText(listDisplay)

    # Begin sorting process
    def sort(self):
        self.sorted_index = 1
        self.optionOneButton.setEnabled(True)
        self.optionTwoButton.setEnabled(True)
        self.setupNextPass()

    # Continue to the next element
    def setupNextPass(self):
        self.current_item = self.rankedList[self.sorted_index]
        self.compare_index = self.sorted_index - 1

        self.setupCompare()

    def setupCompare(self):
        self.optionOneButton.setText(self.rankedList[self.compare_index])
        self.optionTwoButton.setText(self.current_item)
    
    def handleChoice (self, choice):
        if choice == 0:
            self.insert(self.compare_index + 1)
        else:
            if self.compare_index > 0:
                self.compare_index -= 1
                self.setupCompare()
            else:
                self.insert(0)

    # Pop and insert element when something outranks it
    def insert(self, position):
        self.rankedList.pop(self.sorted_index)
        self.rankedList.insert(position, self.current_item)

        self.sorted_index += 1
        self.updateOutputDisplay()

        # Terminate the process once the last elements been ranked
        if self.sorted_index >= len(self.rankedList):
            self.optionOneButton.setText("Option 1")
            self.optionOneButton.setEnabled(False)
            self.optionTwoButton.setText("Option 2")
            self.optionTwoButton.setEnabled(False)
        else:
            self.setupNextPass()