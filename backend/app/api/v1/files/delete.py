from os import remove

from fastapi import HTTPException, Depends

from app.api.v1.router import v1_router
from app.core.base import INSTANCE_PATH
from app.schemas.files import FilesPathResponse
from app.utils.auth import require_api_key


@v1_router.delete("/files/{instance}/{file_path:path}", tags=["Files"], dependencies=[Depends(require_api_key)])
async def delete_file(instance: str, file_path: str) -> FilesPathResponse:
    full_path = INSTANCE_PATH / instance / file_path

    if not full_path.exists() or not full_path.is_file():
        raise HTTPException(status_code=404, detail="File not exists")

    remove(full_path)

    return FilesPathResponse(file_path=str(full_path))
