
from setuptools import setup


setup(
    name="Snake",
    options={
        "build_apps": {
            "include_patterns": [
                "data/fonts/*.ttf",
                "data/models/*.egg",
                "data/sprites/*.png",
            ],
            "gui_apps": {
                "Snake": "main.py",
            },
            "log_filename": "$USER_APPDATA/Snake/output.log",
            "log_append": False,
            "plugins": [
                "pandagl",
            ],
        },
    },
)


