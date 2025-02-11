# import string
# import random
# import pyperclip
 
# output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
 
# print(output_string)
# pyperclip.copy(output_string)

from PyQt6.QtWidgets import QWidget

class RNGString(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Random String Generator")