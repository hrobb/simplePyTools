from PyQt6.QtWidgets import QWidget, QStackedWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt6.QtCore import pyqtSignal

class ToolView(QWidget):
	switched_tool = pyqtSignal(object)
	return_to_main = pyqtSignal()

	def __init__(self, script_registry):
		super().__init__()
		self.script_registry = script_registry
		self.tool_content = QStackedWidget()
		self._init_ui()

	def _init_ui(self):
		# Create sidebar, tool content area
		layout = QHBoxLayout()
		sidebar = self._create_sidebar()
		layout.addWidget(sidebar)
		layout.addWidget(self.tool_content, stretch=1)
		self.setLayout(layout)

	def _create_sidebar(self):
		sidebar = QWidget()
		layout = QVBoxLayout()

		# Return to menu button
		menu_button = QPushButton("Main Menu")
		menu_button.clicked.connect(self.return_to_main.emit)
		layout.addWidget(menu_button)

		# Button for each script
		for script_id, script_info in self.script_registry.items():
			button = QPushButton(script_info.title)
			button.clicked.connect(lambda checked, info=script_info: self.switched_tool.emit(info))
			layout.addWidget(button)

		layout.addStretch()
		sidebar.setLayout(layout)
		sidebar.setStyleSheet("border-right:1px solid rgb(0, 0, 0)")
		sidebar.setFixedWidth(200)
		return sidebar
	
	def get_tool_content(self):
		return self.tool_content




	