from PyQt6.QtWidgets import QWidget, QStackedWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFrame, QLabel
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap

class ToolView(QWidget):
	switched_tool = pyqtSignal(object)
	return_to_main = pyqtSignal()

	def __init__(self, script_registry):
		super().__init__()
		self.script_registry = script_registry
		self.tool_content = QStackedWidget()
		self._init_ui()

	def _init_ui(self):
		# Create sidebar
		layout = QHBoxLayout()
		sidebar = self._create_sidebar()
		layout.addWidget(sidebar)

		# Create divider line
		divider = QFrame()
		divider.setFrameShape(QFrame.Shape.VLine)
		divider.setFrameShadow(QFrame.Shadow.Sunken)
		layout.addWidget(divider)

		# Create tool content area
		layout.addWidget(self.tool_content, stretch=1)
		self.setLayout(layout)

	def _create_sidebar(self):
		sidebar = QWidget()
		layout = QVBoxLayout()

		# Return to menu button
		menu_button = QPushButton("Main Menu")
		menu_button.clicked.connect(self.return_to_main.emit)
		menu_button.setStyleSheet('font: 12pt')
		menu_button.setMinimumHeight(60)
		layout.addWidget(menu_button)
		layout.addSpacing(10)

		# Button for each script
		for script_id, script_info in self.script_registry.items():
			button = QPushButton(script_info.title)
			button.clicked.connect(lambda checked, info=script_info: self.switched_tool.emit(info))
			button.setStyleSheet('font: 10pt')
			button.setMinimumHeight(50)
			layout.addWidget(button)

		# Spacer
		layout.addStretch()
		
		# Logo in bottom corner
		logo_label = QLabel()
		logo = QPixmap("assets/spt.png").scaled(
			150,
			150, 
			Qt.AspectRatioMode.KeepAspectRatio,
			Qt.TransformationMode.SmoothTransformation
		)
		logo_label.setPixmap(logo)
		layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignCenter)

		sidebar.setLayout(layout)
		sidebar.setFixedWidth(220)
		return sidebar
	
	def get_tool_content(self):
		return self.tool_content




	