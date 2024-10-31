from os import mkdir
from pathlib import Path

SAMPLE_CONFIG = {"paths": ["mods"], "auth_token": "123"}
BASE_PATH: Path = Path("/minecraft-cloud-data")
INSTANCE_PATH: Path = BASE_PATH / "instance"
CONFIG_FILE: Path = BASE_PATH / "config.json"

if not INSTANCE_PATH.exists():
    mkdir(INSTANCE_PATH)
