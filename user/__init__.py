from pydantic import BaseModel

class UserRegisterValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: int
    password: str
    city: str


class EditUserValidator(BaseModel):
    user_id: int
    edit_type: str
    new_data: str



