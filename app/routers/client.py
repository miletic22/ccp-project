from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from .. import schemas, oauth2

router = APIRouter(prefix="/client", tags=["Clients"])

@router.get(
    "/",    
    #response_model = schemas.Client,
)
def get_clients(
    db: Session = Depends(get_db), 
    current_user: int = Depends(oauth2.get_current_user),
    
):
    return {"data": "Clients list"}
