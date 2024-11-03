from fastapi import File, UploadFile
from fastapi import HTTPException

from app.api.v1.router import v1_router
from app.core.base import INSTANCE_PATH
from app.schemas.sync import SyncFilePathResponse


@v1_router.post("/files/{directory_path:path}")
async def upload_file(directory_path: str, file: UploadFile = File(...)) -> SyncFilePathResponse:
    destination_path = INSTANCE_PATH / directory_path

    destination_path.mkdir(parents=True, exist_ok=True)

    full_path = destination_path / file.filename

    try:
        with open(full_path, "wb") as f:
            while contents := file.file.read(1024 * 1024):
                f.write(contents)
    except Exception as e:
        raise HTTPException(500, "Failed to save the file.") from e
    finally:
        file.file.close()
    return SyncFilePathResponse(file_path=str(full_path))
