from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.session import db_manager
from app.repositories import cash_flows_repository as repo
from app.schemas import cash_flow as schemas

router = APIRouter(
    prefix="/cash-flows",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/",
    response_model=list[schemas.IndividualCashFlowResponse],
    status_code=200,
)
def read_individual_cash_flows(
    user_id: int, session: Session = Depends(db_manager.get_session)
):
    cash_flow = repo.read_individual_cash_flows(session, user_id)
    return cash_flow


@router.get(
    "/{cash_flow_id}",
    response_model=schemas.IndividualCashFlowResponse,
    status_code=200,
)
def read_individual_cash_flows_by_id(
    user_id: int, cash_flow_id: int, session: Session = Depends(db_manager.get_session)
):
    cash_flow = repo.read_individual_cash_flows_by_id(session, user_id, cash_flow_id)

    if not cash_flow:  # ← 404チェックを追加
        raise HTTPException(status_code=404, detail="Cash flow not found")
    return cash_flow


@router.post(
    "/",
    response_model=schemas.IndividualCashFlowResponse,
    status_code=201,
)
def create_individual_cash_flow(
    user_id: int,
    data: schemas.IndividualCashFlowCreate,
    session: Session = Depends(db_manager.get_session),
):
    try:
        result = repo.create_individual_cash_flow(session, user_id, data)
        return result
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail="Invalid wallet_id or constraint violation"
        )


@router.put(
    "/{cash_flow_id}",
    response_model=schemas.IndividualCashFlowResponse,
    status_code=200,
)
def update_individual_cash_flow(
    user_id: int,
    cash_flow_id: int,
    data: schemas.IndividualCashFlowUpdate,
    session: Session = Depends(db_manager.get_session),
):
    try:
        result = repo.update_individual_cash_flow(session, user_id, cash_flow_id, data)
        if not result:
            raise HTTPException(status_code=404, detail="Cash flow not found")
        return result
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail="Invalid data or constraint violation"
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
