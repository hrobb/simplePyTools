from scripts.rng import RNG
from scripts.rngstring import RNGString

class ToolManager:
	def __init__(self):
		# Dictionary for instantiated tools
		self.tools = {}

	def get_tool(self, script_info):
		# Retrieve tool if it's there, if not create
		if script_info.title not in self.tools:
			tool = self._create_tool(script_info)
			if tool:
				tool.setProperty("script_id", script_info.title)
				self.tools[script_info.title] = tool
		return self.tools.get(script_info.title)
	
	# TODO: Once more are added this should all be read from a dictionary
	def _create_tool(self, script_info):
		if script_info.title == "RNG":
			return RNG()
		elif script_info.title == "RNG String":
			return RNGString()
		return None