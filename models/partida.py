from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

from sqlalchemy.orm import sessionmaker
from random import randint
from database import Session
BaseModel = declarative_base()


class PartidaModel(BaseModel):
    __tablename__ = 'tb_jogos'

    id_partida = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    time1 = sqlalchemy.Column(sqlalchemy.String(25))
    time2 = sqlalchemy.Column(sqlalchemy.String(25))
    data_partida = sqlalchemy.Column(sqlalchemy.String(25))

    def __init__(self, time1, time2, data_partida):
        self.id_partida = randint(1, 9999)
        self.time1 = time1
        self.time2 = time2
        self.data_partida = data_partida

    def json(self):
        return {
            'id_partida': self.id_partida,
            'time1': self.time1,
            'time2': self.time2,
            'data_partida': self.data_partida
        }

    def save_partida(self):
        with Session() as session:
            session.add(self)
            session.commit()
