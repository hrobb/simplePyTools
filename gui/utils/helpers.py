import os
import sys

# Get path to assets
def get_image_path(relative_path):

    if getattr(sys, 'frozen', False):
        # If running from the exe
        base_path = sys._MEIPASS
    else:
        # If running from an interpreter
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relative_path)