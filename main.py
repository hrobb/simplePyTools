import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("SimplePyTools")
		self.setGeometry(100, 100, 800, 600)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())