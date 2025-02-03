import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

class FunctionWidget(QWidget):
	def __init__(self, labelText, parent=None):
		super().__init__(parent)

		# Init variables
		self.label = QLabel(labelText)
		self.button = QPushButton("Launch")

		# Configure layout
		layout = QVBoxLayout()
		layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		
		# Apply layout
		self.setLayout(layout)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("SimplePyTools")
		self.setGeometry(100, 100, 800, 600)

		# Init main container
		appContainer = QWidget()

		# Setup main menu grid
		gridLayout = QGridLayout()

		rows, cols = 2, 4

		for row in range(rows):
			for col in range(cols):
				container = FunctionWidget("Test Function")
				gridLayout.addWidget(container, row, col)

		# Finish setting things up
		appContainer.setLayout(gridLayout)
		self.setCentralWidget(appContainer)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())