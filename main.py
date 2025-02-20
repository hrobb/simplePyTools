import sys
import os
import platform
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from gui.nav_logic.window_manager import MainWindowManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SimplePyTools")
        self.setGeometry(100, 100, 800, 600)
        
        # Get path to the icon
        if getattr(sys, 'frozen', False):
            # If running from the exe
            application_path = sys._MEIPASS
        else:
            # If running from an interpreter
            application_path = os.path.dirname(os.path.abspath(__file__))
            
        icon_name = 'spt.ico' if platform.system() == 'Windows' else 'spt.png'
        icon_path = os.path.join(application_path, 'assets', icon_name)
        self.setWindowIcon(QIcon(icon_path))

        # Init WindowManager
        self.window_manager = MainWindowManager(self)
        self.setCentralWidget(self.window_manager.get_stack())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())