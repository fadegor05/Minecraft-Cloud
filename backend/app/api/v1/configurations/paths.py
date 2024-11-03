from fastapi import Depends

from app.api.v1.router import v1_router
from app.core.config import Config, get_config_dependency
from app.schemas.paths import GetPathsResponse
from app.utils.auth import require_api_key


@v1_router.get("/paths", tags=["Configurations"], dependencies=[Depends(require_api_key)])
async def get_paths(config: Config = Depends(get_config_dependency)) -> GetPathsResponse:
    return GetPathsResponse(paths=config.paths)
