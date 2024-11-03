from os import remove

from fastapi import HTTPException

from app.api.v1.router import v1_router
from app.core.base import INSTANCE_PATH
from app.schemas.sync import SyncFilePathResponse


@v1_router.delete("/files/{file_path:path}", tags=["Files"])
async def delete_file(file_path: str) -> SyncFilePathResponse:
    full_path = INSTANCE_PATH / file_path

    if not full_path.exists() or not full_path.is_file():
        raise HTTPException(status_code=404, detail="File not exists")

    remove(full_path)

    return SyncFilePathResponse(file_path=str(full_path))