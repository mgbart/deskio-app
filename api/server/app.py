from fastapi import FastAPI

from server.routes.asset import router as AssetRouter

app = FastAPI()

app.include_router(AssetRouter, tags=["Asset"], prefix="/asset")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Deskio App!"}
