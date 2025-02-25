from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal

from gui.utils.helpers import get_image_path

class MainMenu(QWidget):
	selected_tool = pyqtSignal(object)

	def __init__(self, script_registry):
		super().__init__()
		self.script_registry = script_registry
		self._init_ui()

	def _init_ui(self):
		layout = QVBoxLayout(self)
		self.setLayout(layout)
		self.setContentsMargins(20, 20, 20, 20)

		layout.addWidget(self._create_title_widget(), 1)
		layout.addWidget(self._create_grid_widget(), 9)
		
	# Create title for main menu
	def _create_title_widget(self):
		container = QWidget()
		container.setMaximumHeight(100)
		layout = QHBoxLayout(container)
		layout.setContentsMargins(0, 0, 0, 0)

		logo_label = QLabel()
		logo = QPixmap(get_image_path("assets/spt.png")).scaled(
			100,
			100, 
			Qt.AspectRatioMode.KeepAspectRatio,
			Qt.TransformationMode.SmoothTransformation
		)
		logo_label.setPixmap(logo)

		title_text = QLabel("SimplePyTools")
		title_text.setStyleSheet('font: 20pt; font-weight:bold')

		layout.addWidget(logo_label)
		layout.addWidget(title_text)
		layout.addStretch(1)

		return container

	# Create a main menu grid for holding each script
	def _create_grid_widget(self):
		
		container = QWidget()
		layout = QGridLayout(container)

		row, col = 0, 0

		for script_id, script_info in self.script_registry.items():
			layout.addWidget(self._create_function_widget(script_info), row, col)
			col = col + 1

		return container

	# Create a widget for each script and place in main menu grid
	def _create_function_widget(self, script_info):
		container = QWidget()
		layout = QVBoxLayout(container)
		layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
		
		return container