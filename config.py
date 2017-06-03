import json
from pathlib import Path

def setup():
    config_dir = Path("config")
    if not config_dir.is_dir():
        config_dir.mkdir()

    usertimes = Path("config/usertime.json")
    if not usertimes.exists():
        with open(usertimes, 'w+') as f:
            empty = dict()
            json.dump(empty, f)
