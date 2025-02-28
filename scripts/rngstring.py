import string
import random
import pyperclip
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QTextEdit
from PyQt6.QtCore import Qt

# Potential future adds: 
# Allow user to define length
# Allow user to define what characters are to be used
# Rolling results history

class RNGString(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Random String Generator")

		self.description = QLabel("Note: Generated strings are automatically copied to the clipboard.")

		self.button = QPushButton("Generate Random String")
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
		layout.addWidget(self.description, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.addSpacing(10)
		layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.addSpacing(10)
		layout.addLayout(row1)

		layout.setAlignment(Qt.AlignmentFlag.AlignTop)

		# Apply layout
		self.setLayout(layout)

	def rollForRNG(self):
		output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
		self.outputBox.setText(output_string)
		pyperclip.copy(output_string)