import sys 
from config.scriptsConfig import SCRIPT_REGISTRY
from gui.sptUI import FunctionWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("SimplePyTools")
		self.setGeometry(100, 100, 800, 600)

		# Init main container
		appContainer = QWidget()

		# Setup main menu grid
		gridLayout = QGridLayout()

		for script_id, script_info in SCRIPT_REGISTRY.items():
			container = FunctionWidget(script_info)
			gridLayout.addWidget(container)

		# Finish setting things up
		appContainer.setLayout(gridLayout)
		self.setCentralWidget(appContainer)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())