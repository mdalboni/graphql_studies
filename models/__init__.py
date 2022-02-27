from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URI = 'sqlite:///db.sqlite3'
engine = create_engine(
    DATABASE_URI,
    convert_unicode=True,
)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


def init_db():
    Model.metadata.create_all(bind=engine)


Model = declarative_base(name='Model')
Model.query = db_session.query_property()

from .pokemon import Pokemon
from .pokemon_data import PokemonData

Model.metadata.create_all(engine)
