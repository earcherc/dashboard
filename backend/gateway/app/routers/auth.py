from fastapi import APIRouter, HTTPException, Depends
from ..services import forward_request
from ..schemas import User
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/register")
async def register(user: User):
    response = await forward_request(
        "auth/register", params=user.dict(), service="auth"
    )
    return response


@router.post("/login")
async def login(data: OAuth2PasswordRequestForm = Depends()):
    response = await forward_request(
        "auth/login", params=data.__dict__, service="auth", is_form_data=True
    )
    return response