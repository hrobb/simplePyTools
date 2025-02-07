from PyQt6.QtWidgets import QWidget, QGridLayout, QStackedWidget
from config.scriptsConfig import SCRIPT_REGISTRY
from gui.FunctionWidget import FunctionWidget

class MainWindowManager:
	def __init__(self, main_window):
		# Init main container
		self.main_window = main_window
		self.stack = QStackedWidget()

		# Init views
		self.main_menu = self.create_main_menu()

		# Add to stack
		self.stack.addWidget(self.main_menu)
		
		# Set initial view
		self.stack.setCurrentWidget(self.main_menu)


	def create_main_menu(self):
		# Setup main menu grid
		menu_widget = QWidget()
		gridLayout = QGridLayout()

		for script_id, script_info in SCRIPT_REGISTRY.items():
			container = FunctionWidget(script_info, self.main_window)
			gridLayout.addWidget(container)

		menu_widget.setLayout(gridLayout)
		return menu_widget
	
	# def create_tool_view()

	# def create_sidebar()
	
	def get_stack(self):
		return self.stack
	
	# def launch_tool()

	# def switch_tool()

	# def return_to_main()