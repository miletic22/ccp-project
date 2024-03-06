from sqlalchemy.sqlalchemy.orm import relationship
from sqlalchemy.sqlalchemy.sql.expression import text
from sqlalchemy.sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

import sqlalchemy.sqlalchemy as sqlalchemy


class User(Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    deleted_at = sqlalchemy.Column(sqlalchemy.TIMESTAMP(timezone=True), nullable=True)
    
    company_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('companies.id'))
    company = relationship("Company", back_populates="user", uselist=False)

class Company(Base):
    __tablename__ = 'companies'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    user_type = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    company_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    development_stage = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    operation_location = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    previous_investors = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.String), nullable=False)
    business_model = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    market_focus = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    sales_revenue = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    sales_growth = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    netprofit = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    netprofit_growth = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    users_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    users_growth = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    costs = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    cost_growth = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    industry_classification = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    funding_amount = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    funding_stage = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    problem_solution = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    website_url = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    startup_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    funding_purpose = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    competition = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.String), nullable=False)
    
    user = relationship("User", back_populates="company", uselist=False)
