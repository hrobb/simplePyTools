import sys 
from gui.WindowManager import MainWindowManager
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("SimplePyTools")
		self.setGeometry(100, 100, 800, 600)

		# Init WindowManager
		self.window_manager = MainWindowManager(self)
		self.setCentralWidget(self.window_manager.get_stack())
		

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())