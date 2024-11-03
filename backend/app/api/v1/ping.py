from app.api.v1.router import v1_router


@v1_router.get("/ping", tags=["Utilities"])
async def ping():
    return {"hello": "world"}
