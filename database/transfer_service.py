from database.models import Transfer,UserCard
from datetime import datetime

from database import get_db

def validate_card(card_number, db):
    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()

    return exact_card


def create_transaction(card_from,card_to,amount):
    db = next(get_db())

    check_card_from = validate_card(card_from, db)
    check_card_to = validate_card(card_to, db)

    if check_card_from and check_card_to:
        if check_card_from.balance >= amount:
            check_card_from.balance -= amount
            check_card_to.balance += amount

            new_transaction = Transfer(card_from_id=check_card_from.card_id,
                                       card_to_id=check_card_to.card_id,
                                       amount=amount,
                                       transaction_date=datetime.now())

            db.add(new_transaction)
            db.commit()

            return 'transaction was successfully made'
        else:
            return 'Not enough money on card'
    else:
        return 'This card does not exists'


def get_card_transaction_db(card_from_id):
    db = next(get_db())

    card_transaction = db.query(Transfer).filter_by(card_from_id=card_from_id).all()

    return card_transaction


def cancel_transfer_db(card_from, card_to, amount, transfer_id):
    db = next(get_db())

    # Проверка на наличие обеих карт в БД
    check_card_from = validate_card(card_from, db)
    check_card_to = validate_card(card_to, db)

    # Если обе карты существуют в бд, проверяем transfer_id
    if check_card_from and check_card_to:
        # Проверяем, существует ли указанный перевод
        transaction_to_cancel = db.query(Transfer).filter_by(trasfer_id=transfer_id).first()
        if transaction_to_cancel:
            # Отмена перевода возвращаем средства к отправителю и убираем их у получателя
            check_card_from.balance += amount
            check_card_to.balance -= amount

            # Удаляем перевод из БД
            db.delete(transaction_to_cancel)
            db.commit()

            return 'Перевод успешно отменен'
        else:
            return 'Указанный перевод не существует'
    else:
        return 'Одна из карт не существует('