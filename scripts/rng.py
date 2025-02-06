import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from PyQt6.QtCore import Qt

class RNG(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Number Generator")

        self.desc = QLabel("Set range for num:")
        self.inpBox = QLineEdit()
        self.inpBox.setPlaceholderText("Max")

        # Configure layout
        layout = QVBoxLayout()
        layout.addWidget(self.desc, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.inpBox, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
        # Apply layout
        self.setLayout(layout)

# while True:
#     x = input("Out of: ")
    
#     if x == '':
#         print("Exiting...")
#         break
    
#     try:
#         result = random.randint(1, int(x))
#         print(result)
#     except ValueError:
#         print("Invalid input. Please enter a number.")


# Subprocess
if __name__ == "__main__":
	subprocess = QApplication(sys.argv)
	module = RNG()
	module.show()
	sys.exit(subprocess.exec())