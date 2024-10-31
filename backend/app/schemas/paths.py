from pydantic import BaseModel
from typing import List


class GetPathsResponse(BaseModel):
    paths: List[str]