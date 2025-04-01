from scripts.rng import RNG
from scripts.rngstring import RNGString
from scripts.subsetSelector import SubsetSelector
from scripts.rnglist import RNGList
from scripts.ranker import ListRanker
from scripts.pacer import Pacer

class ToolManager:
	def __init__(self):
		
		self.active_tools = {}
		self.tool_map = {
			"RNG": RNG,
			"RNG String": RNGString,
			"Subset Selector": SubsetSelector,
			"RNG List Selector": RNGList,
			"List Ranker": ListRanker,
			"Pacer": Pacer
		}

	# Retrieve tool if it's there, if not create it
	def get_tool(self, script_info):
		
		if script_info.title not in self.active_tools:
			tool = self._create_tool(script_info)
			if tool:
				tool.setProperty("script_id", script_info.title)
				self.active_tools[script_info.title] = tool
		return self.active_tools.get(script_info.title)
	
	def _create_tool(self, script_info):

		tool_class = self.tool_map.get(script_info.title)

		if tool_class:
			return tool_class()
		
		return None