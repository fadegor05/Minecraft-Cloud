from typing import List

from pydantic import BaseModel

from app.core.base import CONFIG_FILE, SAMPLE_CONFIG
from app.core.utils import read_json, write_json


class Config(BaseModel):
    paths: List[str]
    auth_token: str

    @classmethod
    async def get_config(cls):
        if not CONFIG_FILE.exists():
            await write_json(SAMPLE_CONFIG, CONFIG_FILE)
        data = await read_json(CONFIG_FILE)
        return cls.parse_obj(data)

    async def save_config(self):
        await write_json(self.dict(), CONFIG_FILE)


async def get_config_dependency():
    return await Config.get_config()
