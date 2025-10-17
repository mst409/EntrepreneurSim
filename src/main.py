from fastapi import FastAPI
from src.database import create_tables
from src.auth import routes as auth
from src.players import routes as players
from src.businesses import routes as businesses

app = FastAPI()
app.include_router(auth.router)
app.include_router(players.router)
app.include_router(businesses.router)


# Create database tables on startup
create_tables()
