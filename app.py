from flask import Flask, jsonify
from flask_restful import Resource, Api
from importlib_metadata import version
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import json
from models.partida import PartidaModel
from sqlalchemy import select
from sqlalchemy import create_engine
from database import Session
from resource.partida import CriarPartidasFutebol, PartidasByName, PartidasByDate, PartidasFutebol, PartidasByParams


app = Flask(__name__)
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'psycopg2:///database'


api = Api(app)
database = SQLAlchemy(app)


# /partidas
api.add_resource(PartidasFutebol, '/partidas')
# /partidas/brasil
api.add_resource(PartidasByName, '/partidas/<string:time>')
# /partidas-data/18/04/2022
api.add_resource(
    PartidasByDate, '/partidas-data/<int:dia>/<int:mes>/<int:ano>')
# /partidas-params?time=Brasil
api.add_resource(PartidasByParams, '/partidas-params')
api.add_resource(CriarPartidasFutebol, '/partidas/')

if __name__ == '__main__':
    app.run(debug=True)
# porta url http://127.0.0.1:5000
