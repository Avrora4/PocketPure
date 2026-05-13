from sqlalchemy.orm import Session

from app.models.cash_flow import IndividualCashFlow
from app.schemas.cash_flow import IndividualCashFlowCreate, IndividualCashFlowUpdate


def read_individual_cash_flows(session: Session, user_id: int):
    """
    Retrieves the individual cash flows for a given user.

    Args:
        Session: The database session to use for the query.
        user_id (int): The ID of the user.

    Returns:
        list: A list of individual cash flows for the user.
    """

    cash_flows = session.query(IndividualCashFlow).filter(
        IndividualCashFlow.user_id == user_id
    )
    return cash_flows.all()


def read_individual_cash_flows_by_id(session: Session, user_id: int, cash_flow_id: int):
    """
    Retrieves the individual cash flows for a given user.

    Args:
        Session: The database session to use for the query.
        user_id (int): The ID of the user.
        cash_flow_id (int): The ID of the cash flow entry.

    Returns:
        IndividualCashFlow: The individual cash flow entry for the user.
    """

    cash_flow = (
        session.query(IndividualCashFlow)
        .filter(
            IndividualCashFlow.user_id == user_id, IndividualCashFlow.id == cash_flow_id
        )
        .first()
    )
    return cash_flow


def create_individual_cash_flow(
    session: Session, user_id: int, data: IndividualCashFlowCreate
):
    """
    Creates a new individual cash flow entry in the database.

    Args:
        Session: The database session to use for the operation.
        user_id (int): The ID of the user for whom the cash flow is being created.
        data (IndividualCashFlowCreate): The data for the new cash flow entry.

    Returns:
        IndividualCashFlow: The created individual cash flow entry.
    """

    new_cash_flow = IndividualCashFlow(**data.model_dump(), user_id=user_id)
    session.add(new_cash_flow)
    session.commit()
    session.refresh(new_cash_flow)

    return new_cash_flow


def update_individual_cash_flow(
    session: Session, user_id: int, cash_flow_id: int, data: IndividualCashFlowUpdate
):
    """
    Updates an existing individual cash flow entry in the database.

    Args:
        session (Session): The database session to use for the operation.
        user_id (int): The ID of the user for whom the cash flow is being updated.
        cash_flow_id (int): The ID of the cash flow entry to update.
        data (IndividualCashFlowUpdate): The updated data for the cash flow entry.

    Returns:
        IndividualCashFlow:
            The updated individual cash flow entry, or None if not found.
    """
    cash_flow = (
        session.query(IndividualCashFlow)
        .filter(
            IndividualCashFlow.id == cash_flow_id, IndividualCashFlow.user_id == user_id
        )
        .first()
    )
    if not cash_flow:
        return None

    update_cash_flow = data.model_dump(exclude_unset=True)

    for key, value in update_cash_flow.items():
        setattr(cash_flow, key, value)

    session.commit()
    session.refresh(cash_flow)
    return cash_flow
