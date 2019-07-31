from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(name,secret_word):
    """Add a user to the DB."""
    user = User(username=name)
    user.hash_password(secret_word)
    session.add(user)
    session.commit()

def get_user(username):
    """Find the first user in the DB, by their username."""
    return session.query(User).filter_by(username=username).first()


def update_fav_food(username, fav_food):
    User_object = session.query(
        User).filter_by(
        username=username).first()
    User_object.fav_food = fav_food
    session.commit()

# update_fav_food("fav_food", True)




