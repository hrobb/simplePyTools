# import string
# import random
# import pyperclip
 
# output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
 
# print(output_string)
# pyperclip.copy(output_string)

import string
import random
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

# TODO: Make it so generated strings are copied to clipboard like in old program

class RNGString(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Random String Generator")
			
		self.inputBox = QLineEdit()
		self.inputBox.setReadOnly(True)
		self.inputBox.setContentsMargins(0, 25, 0, 0)
		self.button = QPushButton("Generate Random String")
		self.button.clicked.connect(self.rollForRNG)

		layout = QVBoxLayout()
		layout.addWidget(self.inputBox, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.setAlignment(Qt.AlignmentFlag.AlignTop)
		self.setLayout(layout)

	def rollForRNG(self):
		output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
		self.inputBox.setText(output_string)