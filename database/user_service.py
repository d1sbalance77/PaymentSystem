from database.models import User


from database import get_db

def register_user(name,surname,phone_number,password,email):
    db = next(get_db())

    new_user = User(name=name,
                        surname=surname,
                        phone_number=phone_number,
                        email=email,
                        password=password)


    db.add(new_user)
    db.commit()

    return 'User was successfully registered'


def get_exact_user_id(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    return exact_user

def check_user_phone_db(phone_number):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        return checker
    else:
        return 'This phone numbver does not exists'


def edit_user_db(user_id,edit_type,new_data):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if exact_user == 'email':
            exact_user_email = new_data
        elif edit_type == 'surname':
            exact_user_surname = new_data

        db.commit()

        return 'User was successfully edited'
    else:
        return 'This user does not exists'



def delete_user_db(user_id):
    db = next(get_db())

    delete_user = db.query(User).filter_by(user_id=user_id).first()

    if delete_user:
        db.delete()
        db.commit()


        return 'User was successfully deleted'
    else:
        return 'User was not successfully deleted'



