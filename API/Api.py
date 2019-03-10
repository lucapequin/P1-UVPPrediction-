#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 23:12:52 2019

@author: andres
"""

from flask import Flask
from flask_restplus import Api, Resource, fields
#from sklearn.externals import joblib
from Forest_AO_deploy import predict_tree

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='API Used Vehicles Price Prediction',
    description='Model for predict the price for used vehicles API.\n Creators:\nAndres Obando\n Luis Carlos Peña\n Klaus Rodriguez\n Alexander Vega')

ns = api.namespace('pricepredict', 
     description='API container')
   
parser = api.parser()

# The variables to input:
# Year', 'Mileage', 'State', 'Make', 'Model'
parser.add_argument(
    'year', 
    type=int, 
    required=True, 
    help='Year of the vehicle', 
    location='args')
parser.add_argument(
    'mileage',
    type=int,
    required=True,
    help='Cumulate mileage',
    location='args')
parser.add_argument(
    'state',
    type=str,
    required=False,
    help='State where vehicle is located',
    location='args')
parser.add_argument(
    'make',
    type=str,
    required=False,
    help='Make of vehicle',
    location='args')
parser.add_argument(
    'model',
    type=str,
    required=False,
    help='model of vehicle',
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PhishingApi(Resource):
# Year', 'Mileage', 'State', 'Make', 'Model'
    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        # For manage the optionals:

        if args['state'] is None:
            args['state'] == 0
        if args['make'] is None:
            args['make'] == 0
        if args['model'] is None:
            args['model'] == 0
        
        p1 = predict_tree(args['year'],args['mileage'],args['state'],args['make'],args['model'])
        
        return {"result": p1}, 200   
app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
