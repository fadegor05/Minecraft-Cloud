import hashlib
import json
from pathlib import Path
from typing import Dict, Union

from utils.checksum import get_file_checksum


def get_dict_hash(data: Dict, algorithm: str = 'sha256') -> str:
    dict_str = json.dumps(data, sort_keys=True)

    hash_func = hashlib.new(algorithm)
    hash_func.update(dict_str.encode('utf-8'))

    return hash_func.hexdigest()


def hash_path(path: Path) -> Union[Dict, str]:
    if path.is_dir():
        items = {}
        for item in path.iterdir():
            if item.is_dir():
                items[item.name] = hash_path(item)
            else:
                items[item.name] = get_file_checksum(item)
        return items
    return get_file_checksum(path)
