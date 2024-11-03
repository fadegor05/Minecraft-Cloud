from fastapi import HTTPException, status, Depends, Security
from fastapi.security.api_key import APIKeyHeader

from app.core.config import get_config_dependency, Config


async def require_api_key(api_key_header: str = Security(APIKeyHeader(name="Authorization", auto_error=False)),
                          config: Config = Depends(get_config_dependency)):
    if api_key_header == config.auth_token:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
