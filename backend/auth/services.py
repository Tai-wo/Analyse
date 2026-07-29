from auth.models import User

from auth.utils import (
    hash_password,
    verify_password
)


def create_user(
    db,
    user_data
):

    hashed = hash_password(
        user_data.password
    )

    user = User(

        username=user_data.username,

        email=user_data.email,

        hashed_password=hashed
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def authenticate_user(
    db,
    email,
    password
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:

        return None

    if not verify_password(
        password,
        user.hashed_password
    ):

        return None

    return user