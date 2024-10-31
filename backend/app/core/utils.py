import json
from pathlib import Path
from typing import Dict


async def write_json(data: Dict, path: Path) -> None:
    async with open(path, "w") as file:
        json.dump(data, file)


async def read_json(path: Path) -> Dict:
    async with open(path, "r") as file:
        data = json.load(file)
    return data
