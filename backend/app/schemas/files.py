from pydantic import BaseModel


class FilesPathResponse(BaseModel):
    file_path: str
