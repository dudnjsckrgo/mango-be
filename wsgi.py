from flask import Flask, jsonify
from flask_restful import Api
from mangotoeic.ext.routes import initialize_routes

app = Flask(__name__)
api = Api(app)


initialize_routes(api)



    