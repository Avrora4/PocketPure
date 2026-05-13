from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import db_manager
from app.repositories import cash_flows_repository as repo
from app.schemas import cash_flow as schemas

router = APIRouter(
    prefix="/cash-flows",
    tags=["users"],
    dependencies=[Depends(db_manager.get_session)],
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

    if not cash_flow:
        raise HTTPException(status_code=404, detail="Cash flows not found")
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

    if not cash_flow:
        raise HTTPException(status_code=404, detail="Cash flows not found")
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
    result = repo.create_individual_cash_flow(session, user_id, data)

    if not result:
        raise HTTPException(status_code=400, detail="Failed to create cash flow")

    return result


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
    result = repo.update_individual_cash_flow(session, user_id, cash_flow_id, data)
    if not result:
        raise HTTPException(status_code=404, detail="Cash flow not found")
    return result
