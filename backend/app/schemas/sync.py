from pydantic import BaseModel


class SyncFilePathResponse(BaseModel):
    file_path: str
