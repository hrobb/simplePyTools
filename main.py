import sys
import os
import platform
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from gui.nav_logic.window_manager import MainWindowManager
from gui.utils.helpers import get_image_path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SimplePyTools")
        self.setGeometry(100, 100, 800, 600)
            
        icon_name = 'spt.ico' if platform.system() == 'Windows' else 'spt.png'
        icon_path = get_image_path(os.path.join('assets', icon_name))
        self.setWindowIcon(QIcon(icon_path))

        # Init WindowManager
        self.window_manager = MainWindowManager(self)
        self.setCentralWidget(self.window_manager.get_stack())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())