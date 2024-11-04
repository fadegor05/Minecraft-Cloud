from pathlib import Path

from network.api_client import ApiClient
from utils.directory import get_instance_hash, delete_recursively, download_recursively
from utils.hash import get_dict_hash


def sync_client(instance_name: str, instance_path: Path) -> bool:
    client = ApiClient()
    paths = client.get_paths()
    instance_hash_tree = get_instance_hash(instance_path, paths)
    instance_hash = get_dict_hash(instance_hash_tree)
    client_sync = client.post_client_sync(instance_name, instance_hash, instance_hash_tree)
    if client_sync is None:
        return False
    delete = client_sync["client_delete"]
    delete_recursively(instance_path, delete)
    download = client_sync["client_download"]
    download_recursively(instance_name, instance_path, download, client)
    return True
