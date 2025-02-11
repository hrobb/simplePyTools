from PyQt6.QtWidgets import QWidget, QGridLayout, QStackedWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from config.scriptsConfig import SCRIPT_REGISTRY
from scripts.rng import RNG
from scripts.rngstring import RNGString

class MainWindowManager:
	def __init__(self, main_window):
		# Init main container
		self.main_window = main_window
		self.stack = QStackedWidget()

		# Init views
		self.main_menu = self.create_main_menu()
		self.tool_view = self.create_tool_view()

		# Add to stack
		self.stack.addWidget(self.main_menu)
		self.stack.addWidget(self.tool_view)
		
		# Set initial view
		self.stack.setCurrentWidget(self.main_menu)


	def create_main_menu(self):
		# Setup main menu grid
		menu_widget = QWidget()
		gridLayout = QGridLayout()

		for script_id, script_info in SCRIPT_REGISTRY.items():
			#container = FunctionWidget(script_info, self.main_window)
			container = QWidget()
			# Init variables
			container.title = QLabel(script_info.title)
			container.desc = QLabel(script_info.description)
			container.button = QPushButton("Launch")
			container.button.clicked.connect(lambda checked, info=script_info: self.launch_tool(info))

			# Configure layout
			containerLayout = QVBoxLayout()
			containerLayout.addWidget(container.title, alignment=Qt.AlignmentFlag.AlignCenter)
			containerLayout.addWidget(container.desc, alignment=Qt.AlignmentFlag.AlignCenter)
			containerLayout.addWidget(container.button, alignment=Qt.AlignmentFlag.AlignCenter)
			containerLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
			
			# Apply layout
			container.setLayout(containerLayout)
			gridLayout.addWidget(container)

		menu_widget.setLayout(gridLayout)
		return menu_widget
	
	
	def create_tool_view(self):
		tool_widget = QWidget()
		layout = QHBoxLayout()

		sidebar = self._create_sidebar()

		self.tool_content = QStackedWidget()

		layout.addWidget(sidebar)
		layout.addWidget(self.tool_content, stretch=1)

		tool_widget.setLayout(layout)
		return tool_widget

	def _create_sidebar(self):
		sidebar = QWidget()
		layout = QVBoxLayout()

		menu_button = QPushButton("Main Menu")
		menu_button.clicked.connect(self.return_to_main)
		layout.addWidget(menu_button)

		for script_id, script_info in SCRIPT_REGISTRY.items():
			button = QPushButton(script_info.title)
			button.clicked.connect(lambda checked, info=script_info: self.switch_tool(info))
			layout.addWidget(button)

		layout.addStretch()
		sidebar.setLayout(layout)
		sidebar.setFixedWidth(200)

		return sidebar
	
	def get_stack(self):
		return self.stack
	
	def launch_tool(self, script_info):
		self.stack.setCurrentWidget(self.tool_view)
		self.switch_tool(script_info)

	def switch_tool(self, script_info):
		for i in range(self.tool_content.count()):
			widget = self.tool_content.widget(i)
			if widget.property("script_id") == script_info.title:
				self.tool_content.setCurrentWidget(widget)
				return

		if script_info.title == "RNG":
			module = RNG()
			module.setProperty("script_id", script_info.title)
			self.tool_content.addWidget(module)
			self.tool_content.setCurrentWidget(module)

		if script_info.title == "RNG String":
			module = RNGString()
			module.setProperty("script_id", script_info.title)
			self.tool_content.addWidget(module)
			self.tool_content.setCurrentWidget(module)

	def return_to_main(self):
		self.stack.setCurrentWidget(self.main_menu)