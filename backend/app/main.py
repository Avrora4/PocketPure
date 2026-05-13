from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.endpoints import router
from app.db.session import db_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_manager.init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
