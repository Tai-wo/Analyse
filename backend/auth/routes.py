from fastapi import APIRouter
from fastapi import Depends

from auth.dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
@router.post("/register")
def register():
    pass
@router.post("/login")
def login():
    pass
@router.get("/me")
def get_profile(

    current_user=Depends(
        get_current_user
    )

):

    return {

        "id": current_user.id,

        "username": current_user.username,

        "email": current_user.email

    }