from pydantic import BaseModel

class AddCardValidator(BaseModel):

    user_id: int
    card_number: int
    balance: float
    card_name: str
    expire_date: int

