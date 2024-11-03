from typing import Dict, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


async def get_dict_diff(dict1: Dict, dict2: Dict) -> (Dict, Dict):
    add = {}
    remove = {}

    for key in dict2:
        if key not in dict1:
            add[key] = dict2[key]
        else:
            if isinstance(dict2[key], dict) and isinstance(dict1[key], dict):
                sub_add, sub_remove = await get_dict_diff(dict1[key], dict2[key])
                if sub_add:
                    add[key] = sub_add
                if sub_remove:
                    remove[key] = sub_remove
            elif dict2[key] != dict1[key]:
                add[key] = dict2[key]
                remove[key] = dict1[key]

    for key in dict1:
        if key not in dict2:
            remove[key] = dict1[key]

    return add, remove


async def get_pydantic_diff(model1: T, model2: T) -> (T, T):
    add, remove = await get_dict_diff(model1.dict(), model2.dict())
    return model1.parse_obj(add), model2.parse_obj(remove)
