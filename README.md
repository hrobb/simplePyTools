# simplePyTools

# Manual Build Steps
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --onefile --icon='assets/spt.png' main.py
