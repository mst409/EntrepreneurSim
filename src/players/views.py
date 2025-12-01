from sqlalchemy import select, text
from sqlalchemy_utils import create_view

from src.auth.models import User
from src.businesses.models import Business
from src.banking.models import BankAccount
from src.database import Base, engine

from .models import Player, players_businesses

# TODO make this more modeler and safe, with handling view already exists error
# Drop the view if it already exists (for SQLite compatibility)
try:
    with engine.begin() as conn:
        conn.execute(text("DROP VIEW IF EXISTS user_view"))
except Exception:
    pass

stmt = select(
    Player.id.label("player_id"),
    User.name.label("name"),
).select_from(Player.__table__.join(User, User.id == Player.user_id))
# for DB thats not SQLite, add 'replace=True'
view = create_view("user_view", stmt, Base.metadata)


try:

    class PlayerView(Base):
        """A view the binds the player_id with the user name"""

        __table__ = view
except Exception as e:
    pass
