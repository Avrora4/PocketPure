from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import app.repositories.cash_flows_repository as cash_flows_repository
from app.db.session import db_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_manager.init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/create_individual_cash_flow")
def create_indivisual_cash_flow_endpoint(
    session: Session = Depends(db_manager.get_session),
):
    cash_flows_repository.create_test_data_individual_cash_flow(session)
    return {"message": "Individual cash flow created successfully"}
