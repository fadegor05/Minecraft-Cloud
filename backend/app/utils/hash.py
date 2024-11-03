import hashlib
import json
from typing import Dict

from pydantic import BaseModel


async def get_dict_hash(data: Dict, algorithm: str = 'sha256') -> str:
    dict_str = json.dumps(data, sort_keys=True)

    hash_func = hashlib.new(algorithm)
    hash_func.update(dict_str.encode('utf-8'))

    return hash_func.hexdigest()


async def get_pydantic_hash(model: BaseModel, algorithm: str = 'sha256') -> str:
    return await get_dict_hash(model.dict(), algorithm)
