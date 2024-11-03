from app.api.v1.router import v1_router
from app.schemas.ping import PingResponse


@v1_router.get("/ping", tags=["Utilities"])
async def ping() -> PingResponse:
    return PingResponse(status="API is up!")
