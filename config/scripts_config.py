from dataclasses import dataclass
from pathlib import Path


@dataclass
class ScriptInfo:
	title: str
	description: str
	path: Path

SCRIPTS_DIR = Path(__file__).parent.parent / "scripts"

SCRIPT_REGISTRY = {
	"RNG": ScriptInfo(
		title="RNG",
		description="Generate a random number",
		path=SCRIPTS_DIR / "rng.py"
	),
	"RNGString": ScriptInfo(
		title="RNG String",
		description="Generate a random string",
		path=SCRIPTS_DIR / "rngstring.py"
	),
	"SubsetSelector": ScriptInfo(
		title="Subset Selector",
		description="Generate a subset of numbers from a given range",
		path=SCRIPTS_DIR / "subsetSelector.py"
	),
	"RNGList": ScriptInfo(
		title="RNG List Selector",
		description="Select a random item from a list",
		path=SCRIPTS_DIR / "rnglist.py"
	),
	"ListRanker": ScriptInfo(
		title="List Ranker",
		description="Algorithmically rank items in a list into an ordered list",
		path=SCRIPTS_DIR / "ranker.py"
	)
}