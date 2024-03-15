from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase, BaseModel):
    password: str


class UserOut(UserBase, BaseModel):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
    

class Client(BaseModel):
    company_name: str
    name: str
    surname: str
    position: str
    development_stage: str
    operation_location: str
    previous_investors: List[str]
    business_model: str
    market_focus: str
    sales_revenue: float
    sales_growth: float
    netprofit: float
    netprofit_growth: float
    users_number: int
    users_growth: float
    costs: float
    cost_growth: float
    industry_classification: str
    funding_amount: float
    funding_stage: str
    problem_solution: str
    website_url: str
    startup_name: str
    funding_purpose: str
    competition: List[str]