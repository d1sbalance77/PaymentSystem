from fastapi import APIRouter

from database.transfer_service import cancel_transfer_db,create_transaction
from transfers import CancelTransactionValidator,CreateTransactionValidator


transaction_router = APIRouter(prefix='/transaction', tags=['Работа с картами'])

@transaction_router.post('/create')
async def add_new_transaction(data: CreateTransactionValidator):
    transaction_data = data.model_dump()

    result = create_transaction(**transaction_data)

    if result:
        return {"message": result}
    else:
        return {"message": 'BIG ERROR '}


@transaction_router.get('/get-transaction')
async def get_transaction_db(card_id: int):

    result = get_transaction_db(card_from_id=card_id)

    if result:
        return result
    else:
        return {"message" 'Big Error'}


@transaction_router.post('/cancel-transaction')
async def cancel_transaction(data: CancelTransactionValidator):

    cancel_data = data.model_dump()
    result = cancel_transfer_db(**cancel_data)

    if result:
        return {"message": result}
    else:
        return {"message": "Big Error"}