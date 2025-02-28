from pathlib import Path
import sys

# Get path to assets
def get_image_path(relative_path):

    if getattr(sys, 'frozen', False):
        # If running from the exe
        base_path = Path(sys._MEIPASS)
    else:
        # If running from an interpreter
        base_path = Path(__file__).resolve().parents[2]
    
    return str(base_path / relative_path)