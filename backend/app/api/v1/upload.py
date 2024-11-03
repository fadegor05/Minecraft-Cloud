from http.client import HTTPException

from fastapi import File, UploadFile

from app.api.v1.router import v1_router
from app.core.base import INSTANCE_PATH


@v1_router.post("/sync/upload/{file_path:path}")
async def post_sync_upload_file(file_path: str, file: UploadFile = File(...)):
    destination_path = INSTANCE_PATH / file_path

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
    return {"message": f"Successfully uploaded {file.filename}"}
