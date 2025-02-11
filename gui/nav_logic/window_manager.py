from PyQt6.QtWidgets import QStackedWidget
from config.scriptsConfig import SCRIPT_REGISTRY
from gui.nav_logic.tool_manager import ToolManager
from gui.views.main_menu import MainMenu
from gui.views.tool_view import ToolView

class MainWindowManager:
	def __init__(self, main_window):
		# Init main container, nav logic
		self.main_window = main_window
		self.stack = QStackedWidget()
		self.tool_manager = ToolManager()

		# Init views
		self.main_menu = MainMenu(SCRIPT_REGISTRY)
		self.tool_view = ToolView(SCRIPT_REGISTRY)

		# Hook up slot/signal
		self.main_menu.selected_tool.connect(self.launch_tool)
		self.tool_view.switched_tool.connect(self.switch_tool)
		self.tool_view.return_to_main.connect(self.return_to_main)

		# Add to stack
		self.stack.addWidget(self.main_menu)
		self.stack.addWidget(self.tool_view)
		
		# Set initial view
		self.stack.setCurrentWidget(self.main_menu)
	
	def get_stack(self):
		return self.stack
	
	def launch_tool(self, script_info):

		self.stack.setCurrentWidget(self.tool_view)
		self.switch_tool(script_info)

	def switch_tool(self, script_info):
		# Grab existing tool content
		tool_content = self.tool_view.get_tool_content()

		# Check stack to see if called tool is created
		for i in range(tool_content.count()):
			widget = tool_content.widget(i)
			if widget.property("script_id") == script_info.title:
				tool_content.setCurrentWidget(widget)
				return

		# Init and set the called tool
		tool = self.tool_manager.get_tool(script_info)
		if tool:
			tool_content.addWidget(tool)
			tool_content.setCurrentWidget(tool)

	def return_to_main(self):
		self.stack.setCurrentWidget(self.main_menu)