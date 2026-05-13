from fastapi import APIRouter

from . import cash_flows

router = APIRouter()

router.include_router(cash_flows.router, prefix="/users/{user_id}", tags=["users"])
