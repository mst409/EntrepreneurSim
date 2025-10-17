from pydantic import BaseModel, Field, UUID4


class AccountTypes(enumerate):
    Player = 'player'
    Buisness = 'buisness'


class BaseBankAccount(BaseModel):
    capital: float = Field(default=30.00)
    type: AccountTypes

class BankAccountREsponse(BaseBankAccount):
    id : UUID4


class BaseTransaction(BaseModel):
    amount: float
    from_acc: UUID4
    to_acc: UUID4