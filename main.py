import sys 
from gui.sptUI import FunctionWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout

scripts = {"RNG": "/scripts/rng.py"}

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("SimplePyTools")
		self.setGeometry(100, 100, 800, 600)

		# Init main container
		appContainer = QWidget()

		# Setup main menu grid
		gridLayout = QGridLayout()

		for label, path in scripts.items():
			container = FunctionWidget(label, path)
			gridLayout.addWidget(container)

		# Finish setting things up
		appContainer.setLayout(gridLayout)
		self.setCentralWidget(appContainer)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())