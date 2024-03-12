from fastapi import FastAPI
#from .routers import auth, budget, category, transaction, user
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, SessionLocal
from . import  models

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.include_router(budget.router)
#app.include_router(user.router)
#app.include_router(auth.router)
#app.include_router(category.router)
#app.include_router(transaction.router)
