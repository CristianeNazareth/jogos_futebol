from flask import Flask, jsonify
from flask_restful import Resource, Api
from importlib_metadata import version
from flask_sqlalchemy import SQLAlchemy
import json
# from resource.jogo import Partidas_Futebol
from models.partida import PartidaModel
from sqlalchemy import select
from sqlalchemy import create_engine
from database import Session

app = Flask(__name__)
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'psycopg2:///database'


api = Api(app)
# database = SQLAlchemy(app)


class Partidas_Futebol(Resource):
    def get(self):

        session = Session()

        query_result = select(PartidaModel)

        partidas = []
        for partida in session.scalars(query_result):
            partidas.append(partida.json())

        session.close()
        return partidas
        # return {'partidas': "minhas partidas"}


api.add_resource(Partidas_Futebol, '/partidas')


if __name__ == '__main__':
    app.run(debug=True)
# porta url http://127.0.0.1:5000
