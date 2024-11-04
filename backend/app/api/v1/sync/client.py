from fastapi import Depends, HTTPException

from app.api.v1.router import v1_router
from app.core.base import INSTANCE_PATH
from app.core.config import Config, get_config_dependency
from app.schemas.sync import SyncClientBody, SyncClientResponse
from app.utils.auth import require_api_key
from app.utils.dict import get_pydantic_diff
from app.utils.hash import get_pydantic_hash
from app.utils.path import get_directory_hash


@v1_router.post("/sync/client/{instance}", tags=["Sync"], dependencies=[Depends(require_api_key)])
async def sync_client(instance: str, body: SyncClientBody,
                      config: Config = Depends(get_config_dependency)) -> SyncClientResponse:
    # TODO: Add caching, if server_hash == client_hash
    full_path = INSTANCE_PATH / instance
    if not full_path.exists():
        raise HTTPException(status_code=404, detail="Instance not found")
    server_hash_tree = await get_directory_hash(full_path, config.paths)
    server_hash = await get_pydantic_hash(server_hash_tree)
    download, delete = await get_pydantic_diff(body.client_hash_tree, server_hash_tree)
    return SyncClientResponse(server_hash=server_hash, server_hash_tree=server_hash_tree, client_download=download,
                              client_delete=delete)
