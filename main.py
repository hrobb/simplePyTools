import sys 
from gui.nav_logic.window_manager import MainWindowManager
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("SimplePyTools")
		self.setWindowIcon(QIcon('assets/spt.png'))
		self.setGeometry(100, 100, 800, 600)

		# Init WindowManager
		self.window_manager = MainWindowManager(self)
		self.setCentralWidget(self.window_manager.get_stack())
		

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())