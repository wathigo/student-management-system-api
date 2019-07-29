""" Third party imports"""
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

""" Local imports"""
from ..models.models_parent import ParentModels

class Parent(Resource):
    """User record endpoints"""
    def __init__(self):
        self.models = ParentModels()

    def post(self):
        """ test working endpoint """
        json_data = request.get_json()
        return self.models.save_new_parent(json_data)
