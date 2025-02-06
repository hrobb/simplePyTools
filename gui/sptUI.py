import sys, subprocess
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
from config.scriptsConfig import ScriptInfo

class FunctionWidget(QWidget):
	def __init__(self, script_info: ScriptInfo, parent=None):
		super().__init__(parent)

		# Init variables
		self.title = QLabel(script_info.title)
		self.desc = QLabel(script_info.description)
		self.button = QPushButton("Launch")
		self.button.clicked.connect(lambda: self.launch_script(script_info.path))

		# Configure layout
		layout = QVBoxLayout()
		layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.addWidget(self.desc, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		
		# Apply layout
		self.setLayout(layout)

	def launch_script(self, scriptPath):
		try:
			#print(scriptPath)
			#subprocess.Popen([sys.executable, scriptPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

			process = subprocess.Popen([sys.executable, scriptPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE
			)
			output, error = process.communicate(timeout=5)  # Wait 5 sec for output
			print("Output:", output.decode())
			print("Error:", error.decode())
		except Exception as e:
			print(f"Error launching {scriptPath}: {e}")