# from importlib.resources import path
import json
# from mimetypes import init
from os import times
# from re import S
# from readline import append_history_file
from sqlalchemy.orm import sessionmaker
from flask import jsonify, request, session
from flask_restful import Resource, reqparse
import psycopg2
from database import Session
from sqlalchemy import select
from models.partida import PartidaModel
from sqlalchemy import or_


argumentos = reqparse.RequestParser()
argumentos.add_argument('time1', type=str, required=True,
                        help="The field 'time1' cannot be left blank")
argumentos.add_argument('time2', type=str, required=True,
                        help="The field 'time2' cannot be left blank")
argumentos.add_argument('data_partida', type=str, required=True,
                        help="The field 'time1' cannot be left blank")


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


class CriarPartidasFutebol(Resource):

    def post(self):
        times = []
        dados = json.loads(request.data)
        times.append(dados)       
        partida = PartidaModel(**dados)        
        partida.save_partida()       
        return partida
        return {"message": f"Created '{dados['time1']}' x '{dados['time2']}' whith success"}, 201

    # def post(self):
    #     dados = request.json
    #     partida = PartidaModel(time1=dados['time1'], time2=dados['time2'], data_partida=dados['data_partida'])
    #     partida.save_partida()
    #     time = {
    #         'id_partida': partida.id_partida,
    #         'time1': partida.time1,
    #         'time2': partida.time2,
    #         'data_partida': partida.data_partida
    #     }
    #     return time