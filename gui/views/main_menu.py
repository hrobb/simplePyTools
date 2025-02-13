from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal

class MainMenu(QWidget):
	selected_tool = pyqtSignal(object)

	def __init__(self, script_registry):
		super().__init__()
		self.script_registry = script_registry
		self._init_ui()

	def _init_ui(self):
		# Create a widget for each script and place in main menu grid
		layout = QGridLayout()
		row, col = 0, 0

		for script_id, script_info in self.script_registry.items():
			container = self._create_function_widget(script_info)
			layout.addWidget(container, row, col)
			col = col + 1

		self.setContentsMargins(50, 100, 50, 100)
		self.setLayout(layout)

	def _create_function_widget(self, script_info):
		container = QWidget()
		layout = QVBoxLayout()

		title = QLabel(script_info.title)
		title.setStyleSheet('font: 12pt')
		desc = QLabel(script_info.description)
		button = QPushButton("Launch")
		button.setMinimumSize(60, 35)
		button.clicked.connect(lambda: self.selected_tool.emit(script_info))

		layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.addWidget(desc, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.addSpacing(15)
		layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)
		layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

		container.setLayout(layout)
		return container