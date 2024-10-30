from app.api.v1 import v1_router


@v1_router.get("/ping")
async def ping():
    return {"hello": "world"}