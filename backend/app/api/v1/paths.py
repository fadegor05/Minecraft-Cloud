from fastapi import Depends

from app.api.v1 import v1_router
from app.core.config import Config, get_config_dependency
from app.schemas.paths import GetPathsResponse


@v1_router.get("/paths")
async def get_paths(config: Config = Depends(get_config_dependency)):
    return GetPathsResponse(paths=config.paths)
