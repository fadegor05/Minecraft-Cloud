from fastapi import File, UploadFile
from fastapi import HTTPException, Depends

from app.api.v1.router import v1_router
from app.core.base import INSTANCE_PATH
from app.schemas.files import FilesPathResponse
from app.utils.auth import require_api_key


@v1_router.post("/files/{instance}/{directory_path:path}", tags=["Files"], dependencies=[Depends(require_api_key)])
async def upload_file(instance: str, directory_path: str, file: UploadFile = File(...)) -> FilesPathResponse:
    destination_path = INSTANCE_PATH / instance / directory_path

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
    return FilesPathResponse(file_path=str(full_path))
