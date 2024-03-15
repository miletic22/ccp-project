from sqlalchemy.orm import relationship
from .database import Base
import sqlalchemy as sqlalchemy


class User(Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP(timezone=True), nullable=False, server_default=sqlalchemy.func.now())
    updated_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP(timezone=True), nullable=False)
    deleted_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP(timezone=True), nullable=True)
    
    company_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('companies.id'))
    company = relationship("Company", back_populates="user", uselist=False)

class Company(Base):
    __tablename__ = 'companies'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    user_type = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    company_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    development_stage = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    operation_location = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    previous_investors = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.String), nullable=True)
    business_model = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    market_focus = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    sales_revenue = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    sales_growth = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    netprofit = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    netprofit_growth = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    users_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    users_growth = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    costs = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    cost_growth = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    industry_classification = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    funding_amount = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    funding_stage = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    problem_solution = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    website_url = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    startup_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    funding_purpose = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    competition = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.String), nullable=True)
    
    user = relationship("User", back_populates="company", uselist=False)
