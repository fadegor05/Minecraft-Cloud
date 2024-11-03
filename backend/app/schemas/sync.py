from typing import Dict, Union

from pydantic import BaseModel, RootModel


class FilesHashTree(RootModel):
    root: Dict[str, Union[str, "FilesHashTree"]]


class SyncBody(BaseModel):
    client_hash: str
    client_hash_tree: FilesHashTree


class SyncResponse(BaseModel):
    server_hash: str
    server_hash_tree: FilesHashTree


class SyncClientBody(SyncBody):
    pass


class SyncServerBody(SyncBody):
    pass


class SyncClientResponse(SyncResponse):
    client_download: FilesHashTree
    client_delete: FilesHashTree


class SyncServerResponse(SyncResponse):
    server_upload: FilesHashTree
    server_delete: FilesHashTree
