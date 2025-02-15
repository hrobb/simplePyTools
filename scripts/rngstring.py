import string
import random
import pyperclip
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class RNGString(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Random String Generator")

		self.description = QLabel("Note: Generated strings are automatically copied to the clipboard.")
			
		self.outputBox = QLineEdit()
		self.outputBox.setReadOnly(True)

		self.button = QPushButton("Generate Random String")
		self.button.setFixedSize(200, 30)
		self.button.clicked.connect(self.rollForRNG)

		# Configure layout
		layout = QVBoxLayout()

		layout.addSpacing(20)
		layout.addWidget(self.description, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.addSpacing(10)
		layout.addWidget(self.outputBox, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.addSpacing(10)
		layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)

		layout.setAlignment(Qt.AlignmentFlag.AlignTop)

		# Apply layout
		self.setLayout(layout)

	def rollForRNG(self):
		output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
		self.outputBox.setText(output_string)
		pyperclip.copy(output_string)