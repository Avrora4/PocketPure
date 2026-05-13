from datetime import datetime

from pydantic import BaseModel, field_validator


class IndividualCashFlowCreate(BaseModel):
    name: str
    amount: int
    direction: int
    wallet_id: int
    transaction_date: datetime
    comment: str | None = None

    @field_validator("amount")
    def validate_amount(cls, value):
        if value <= 0:
            raise ValueError("Amount must be a positive integer")
        return value

    @field_validator("direction")
    def validate_direction(cls, value):
        if value not in (0, 1):
            raise ValueError("Direction must be either 0 (income) or 1 (expense)")
        return value


class IndividualCashFlowUpdate(IndividualCashFlowCreate):
    name: str | None = None
    amount: int | None = None
    direction: int | None = None
    wallet_id: int | None = None
    transaction_date: datetime | None = None
    comment: str | None = None

    @field_validator("amount")
    def validate_amount(cls, value):
        if value is not None and value <= 0:
            raise ValueError("Amount must be a positive integer")
        return value

    @field_validator("direction")
    def validate_direction(cls, value):
        if value is not None and value not in (0, 1):
            raise ValueError("Direction must be either 0 (income) or 1 (expense)")
        return value


class IndividualCashFlowResponse(IndividualCashFlowCreate):
    model_config = {"from_attributes": True}

    id: int
    user_id: int
    name: str
    amount: int
    direction: int
    wallet_id: int
    transaction_date: datetime
    comment: str | None = None
    created_at: datetime
    updated_at: datetime
