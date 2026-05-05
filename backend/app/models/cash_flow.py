from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Integer, SmallInteger, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class IndividualCashFlow(Base):
    __tablename__ = "individual_cash_flow"

    # Define the columns for the individual_cash_flow table

    # id : Record the unique identifier for each cash flow entry
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    # user_id : Record the ID of the user associated with the cash flow entry
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)

    # name : Record the name or description of the cash flow entry
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    # amount : Record the amount of the cash flow entry
    amount: Mapped[int] = mapped_column(BigInteger, nullable=False)

    # direction : Record the direction of the cash flow entry
    # (e.g., 0 for income, 1 for expense)
    direction: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    # wallet_id : Record the ID of the wallet associated with the cash flow entry
    wallet_id: Mapped[int] = mapped_column(Integer, nullable=False)

    # transaction_date : Record the using cash date and time of the cash flow entry
    transaction_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    # comment : Record any additional comments or notes about the cash flow entry
    comment: Mapped[str] = mapped_column(Text, nullable=True)

    # created_at : Record the date and time when the cash flow entry was created
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    # updated_at : Record the date and time when the cash flow entry was last updated
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
