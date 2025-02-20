# SimplePyTools

A GUI-wrapped collection of Python utility scripts that works for both Windows and Linux.

## Features
- RNG Scripts
    - Random number generator
    - Random string generator
- More scripts coming soon

## Installation

### Setup Virtual Environment (from source)
```bash
# Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# Update pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller
```

### Build Instructions

Delete previous builds (`build` and `dist`) if they exist

#### Windows
```bash
pyinstaller --windowed --name SimplePyTools --icon=assets/spt.ico --add-data "assets;assets" main.py
```

#### Linux
```bash
pyinstaller --onefile --name SimplePyTools --icon=assets/spt.png --add-data "assets:assets" main.py
```

The output will be an executable in the `dist` directory.