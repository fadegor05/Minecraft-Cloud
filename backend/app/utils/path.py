from pathlib import Path
from typing import List

from app.schemas.sync import FilesHashTree
from app.utils.checksum import get_file_checksum


async def hash_path(path: Path) -> FilesHashTree:
    if path.is_dir():
        items = {}
        for item in path.iterdir():
            if item.is_dir():
                items[item.name] = await hash_path(item)
            else:
                items[item.name] = await get_file_checksum(item)
        return FilesHashTree.parse_obj(items)
    raise NotADirectoryError(f"{path} is not a directory")


async def get_directory_hash(directory_path: Path, include_only_paths: List[str]) -> FilesHashTree:
    if not directory_path.exists() or not directory_path.is_dir():
        raise FileNotFoundError(f"directory: {directory_path} is not exists")
    paths_hashes = {}
    for path in include_only_paths:
        current_path = directory_path / path
        if current_path.exists() and current_path.is_dir():
            paths_hashes[current_path.name] = await hash_path(current_path)
        elif current_path.exists() and current_path.is_file():
            paths_hashes[current_path.name] = await get_file_checksum(current_path)

    return FilesHashTree.parse_obj(paths_hashes)
