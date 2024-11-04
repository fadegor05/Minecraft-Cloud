from os import remove
from pathlib import Path
from typing import List, Dict

from network.api_client import ApiClient
from utils.checksum import get_file_checksum
from utils.hash import hash_path


def get_instance_hash(instance_path: Path, include_only_paths: List[str]) -> Dict:
    if not instance_path.exists() or not instance_path.is_dir():
        raise FileNotFoundError(f"Minecraft instance directory: {instance_path} is not exists")
    paths_hashes = {}
    for path in include_only_paths:
        current_path = instance_path / path
        if current_path.exists() and current_path.is_dir():
            paths_hashes[current_path.name] = hash_path(current_path)
        elif current_path.exists() and current_path.is_file():
            paths_hashes[current_path.name] = get_file_checksum(current_path)

    return paths_hashes


def delete_recursively(current_path: Path, items: Dict):
    for item in items:
        full_path = current_path / item
        if full_path.is_exists() and full_path.is_file():
            remove(full_path)
        elif full_path.is_exists() and full_path.is_dir():
            delete_recursively(full_path, items[item])


def download_recursively(instance_name: str, current_path: Path, items: Dict, api_client: ApiClient,
                         server_path: Path = Path("/")):
    for item in items:
        full_path = current_path / item
        if isinstance(items[item], dict):
            full_path.mkdir()
            download_recursively(instance_name, full_path, items[item], api_client, server_path / item)
        else:
            api_client.get_download_file(instance_name, str(server_path / item), full_path)
