from fastapi import FastAPI
from src.database import create_tables
from src.auth import routes as auth

app = FastAPI()
app.include_router(auth.router)


# Create database tables on startup
create_tables()
