from sqlalchemy import create_engine
from config import DATABASE_URI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

# debug
# database = create_engine(DATABASE_URI, echo=True)
database = create_engine(DATABASE_URI)

Session = sessionmaker(bind=database)


def recreate_database():
    Base.metadata.drop_all(database)
    Base.metadata.create_all(database)
