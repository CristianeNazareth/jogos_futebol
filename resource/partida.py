from importlib.resources import path
from re import S
from readline import append_history_file
from flask import session
from flask_restful import Resource, reqparse
import psycopg2
from database import Session
from sqlalchemy import select
from models.partida import PartidaModel
from sqlalchemy import or_


class PartidasFutebol(Resource):
    def get(self):

        session = Session()
        query_result = select(PartidaModel)

        partidas = []
        for partida in session.scalars(query_result):
            partidas.append(partida.json())

        session.close()
        return partidas
        # return {'partidas': "minhas partidas"}


class PartidasByName(Resource):
    def get(self, time):

        session = Session()
        query_result = select(PartidaModel).where(
            or_(PartidaModel.time1 == time, PartidaModel.time2 == time))

        partidas = []
        for partida in session.scalars(query_result):
            partidas.append(partida.json())

        session.close()
        return partidas


class PartidasByDate(Resource):
    def get(self, dia, mes, ano):

        # 18/04/2022
        date = f'{dia:02d}/{mes:02d}/{ano}'

        session = Session()
        query_result = select(PartidaModel).where(
            PartidaModel.data_partida == date)

        partidas = []
        for partida in session.scalars(query_result):
            partidas.append(partida.json())

        session.close()
        return partidas


class PartidasByParams(Resource):
    def get(self):

        path_params = reqparse.RequestParser()
        path_params.add_argument(
            'time', type=str, required=False, location='args')

        time = path_params.parse_args()['time']
    
        session = Session()
        query_result = select(PartidaModel).where(
            or_(PartidaModel.time1 == time, PartidaModel.time2 == time))

        partidas = []
        for partida in session.scalars(query_result):
            partidas.append(partida.json())

        session.close()
        return partidas