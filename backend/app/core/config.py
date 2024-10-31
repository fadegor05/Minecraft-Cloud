from pathlib import Path
from app.core.utils import write_json

BASE_FOLDER = Path("/minecraft-cloud-data")
INSTANCE_FOLDER = BASE_FOLDER / "instance"
CONFIG_FILE = BASE_FOLDER / "config.json"
SAMPLE_CONFIG = {
    "paths": [
        "mods"
    ],
    "auth_token": "123"
}

if not CONFIG_FILE.exists():
    write_json(SAMPLE_CONFIG, CONFIG_FILE)
