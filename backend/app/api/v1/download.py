from fastapi import HTTPException
from fastapi.responses import FileResponse

from app.api.v1.router import v1_router
from app.core.base import INSTANCE_PATH


@v1_router.get("/sync/download/{file_path:path}")
async def get_sync_download_file(file_path: str) -> FileResponse:
    full_path = INSTANCE_PATH / file_path

    if not full_path.exists() or not full_path.is_file():
        raise HTTPException(status_code=404, detail="File not exists")

    return FileResponse(full_path)
