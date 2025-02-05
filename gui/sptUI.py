import sys, subprocess
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

class FunctionWidget(QWidget):
	def __init__(self, labelText, scriptPath, parent=None):
		super().__init__(parent)

		# Init variables
		self.label = QLabel(labelText)
		self.button = QPushButton("Launch")
		self.button.clicked.connect(lambda: self.launch_script(scriptPath))

		# Configure layout
		layout = QVBoxLayout()
		layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		
		# Apply layout
		self.setLayout(layout)

	def launch_script(self, scriptPath):
		try:
			subprocess.Popen([sys.executable, scriptPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		except Exception as e:
			print(f"Error launching {scriptPath}: {e}")