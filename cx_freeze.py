import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = None

setup(  name = "Amir",
        version = "0.1",
        description = "Open CV Exe Test",
        options = {"portScanner": build_exe_options},
        executables = [Executable("portScan.py", base=base)])