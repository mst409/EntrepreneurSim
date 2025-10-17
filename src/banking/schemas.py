from pydantic import BaseModel, Field, UUID4


class AccountTypes(enumerate):
    Player = 'player'
    Buisness = 'buisness'


class BaseBankAccount(BaseModel):
    capital: float | None = Field(default=30.00)
    account_number: int = Field(max_digits=10)
    # roll: AccountTypes
class BankAccountResponse(BaseBankAccount):
    id : UUID4


class BaseTransaction(BaseModel):
    amount: float
    from_acc: UUID4
    to_acc: UUID4