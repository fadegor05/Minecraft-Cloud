from fastapi import Depends

from app.api.v1.router import v1_router
from app.core.base import INSTANCE_PATH
from app.core.config import Config, get_config_dependency
from app.schemas.sync import SyncServerBody, SyncServerResponse
from app.utils.auth import require_api_key
from app.utils.dict import get_pydantic_diff
from app.utils.hash import get_pydantic_hash
from app.utils.path import get_directory_hash


@v1_router.post("/sync/server", tags=["Sync"], dependencies=[Depends(require_api_key)])
async def sync_server(body: SyncServerBody, config: Config = Depends(get_config_dependency)) -> SyncServerResponse:
    # TODO: Add caching, if server_hash == client_hash
    server_hash_tree = await get_directory_hash(INSTANCE_PATH, config.paths)
    server_hash = await get_pydantic_hash(server_hash_tree)
    upload, delete = await get_pydantic_diff(server_hash_tree, body.client_hash_tree)
    return SyncServerResponse(server_hash=server_hash, server_hash_tree=server_hash_tree, server_upload=upload,
                              server_delete=delete)
