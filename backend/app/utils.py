from fastapi import HTTPException, status
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):

    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:

    return pwd_context.verify(plain_password, hashed_password)
  

def check_existence(
    obj,
    custom_message: str = None,
    expect_existence: bool = False,
    custom_status_code: int = None,
):
    if expect_existence and obj:
        detail_message = (
            custom_message if custom_message else f"{type(obj).__name__} already exists"
        )
        raise HTTPException(
            status_code=custom_status_code or status.HTTP_400_BAD_REQUEST,
            detail=detail_message,
        )
    elif not expect_existence and not obj:
        detail_message = (
            custom_message if custom_message else f"{type(obj).__name__} not found"
        )
        raise HTTPException(
            status_code=custom_status_code or status.HTTP_404_NOT_FOUND,
            detail=detail_message,
        )


def check_deleted(obj):

    if hasattr(obj, "deleted_at") and obj.deleted_at:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{type(obj).__name__} is deleted",
        )