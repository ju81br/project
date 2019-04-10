#!/usr/local/bin python
""" Flask api (docstring)"""

import logging as log
from flask import Flask, request
from flask_restful import Resource, Api
from webservice import yaml_loader, get_city, get_average

app = Flask(__name__)
api = Api(app)
log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)
CONFIG_PATH = 'config.yml'


class City(Resource):
    """ class for all /cidade requests (docstring) """

    def get(self):
        log.info('received a new request - /cidade')
        id_city = request.args.get('id')
        err, msg = get_city(id_city)

        if not err:
            return {'error': msg}, 400

        return {'message': 'success'}, 200


class Analyze(Resource):
    """ class for all /analise requests (docstring) """

    def get(self):
        log.info('received a new request - /analise')
        date_initial = request.args.get('data_inicial')
        date_final = request.args.get('data_final')
        err, result = get_average(date_initial, date_final)

        if not err:
            return {'error': err}, 400

        return result, 200


api.add_resource(City, '/cidade')
api.add_resource(Analyze, '/analise')

@app.before_first_request
def startup():
    """ read yaml file before first request (docstring) """
    yaml_loader(CONFIG_PATH)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
