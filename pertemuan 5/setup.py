import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages" : ["pygame"],
    "include_files": ["ball.png", "paddle.png", "pong.ogg", "score.ogg"]
}

base = None
if sys.platform == "win32":
    base = "win32GUI"
    
setup(
    name = "Kreshna Putra",
    version = "0.1",
    description = "Pong Game",
    options = {"build_exe": build_exe_options},
    executables = [Executable("pong.py", base=base)]
)