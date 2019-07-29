""" import the necessary modules"""
from flask_restful import Api
from flask import Blueprint

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)

""" import classes containg the endpoints """
from .views.views_parent import Parent

api.add_resource(Parent, '/register/parent')
