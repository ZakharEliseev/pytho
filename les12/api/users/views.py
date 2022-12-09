from fastapi import APIRouter, HTTPException
from starlette import status

from .schemes import UserOut, UserIn

from . import crud

router = APIRouter(prefix='/users',
                   tags=['Users'])


@router.get("", response_model=list[UserOut])
def list_users() -> list[UserOut]:
    return crud.get_users()


@router.post('', response_model=UserOut)
def create_user(user_in: UserIn) -> UserOut:
    return crud.create_user(user_in)


@router.get("/{user_id}", response_model=UserOut)
def list_users(user_id: int) -> UserOut:
    user = crud.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= f'user #{user_id} doesn"t exist!'
    )
