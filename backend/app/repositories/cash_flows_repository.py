from datetime import datetime

from sqlalchemy.orm import Session

from app.models.cash_flow import IndividualCashFlow


def get_indivisual_cash_flows(session: Session, user_id: int):
    """
    Retrieves the indivisual cash flows for a given user.

    Args:
        Session: The database session to use for the query.
        user_id (int): The ID of the user.

    Returns:
        list: A list of indivisual cash flows for the user.
    """

    cash_flows = session.query(IndividualCashFlow).filter(
        IndividualCashFlow.user_id == user_id
    )
    return cash_flows.all()


def create_test_data_individual_cash_flow(session: Session):
    """
    Creates a new individual cash flow entry in the database.

    Args:
        user_id (int): The ID of the user associated with the cash flow entry.
        name (str): The name or description of the cash flow entry.
        amount (int): The amount of the cash flow entry.
        direction (int): The direction of the cash flow entry
        (e.g., 0 for income, 1 for expense).
        wallet_id (int): The ID of the wallet associated with the cash flow entry.
        transaction_date (datetime): The date and time of the cash flow transaction.
        comment (str, optional): Additional comments or notes about the cash flow entry.

    Returns:
        IndivisualCashFlow: The created individual cash flow entry.
    """

    new_cash_flow = IndividualCashFlow(
        user_id=1,
        name="Test Cash Flow",
        amount=1000,
        direction=0,
        walled_id=1,
        transaction_date="2024-01-01 12:00:00",
        comment="This is a test cash flow entry.",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    session.add(new_cash_flow)
    session.commit()
    session.refresh(new_cash_flow)
    return new_cash_flow
