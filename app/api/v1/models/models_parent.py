""" Third party imports"""
import datetime

""" local imports"""
from app.utils.database.schemas import Parent
from .models_base import BaseModels


class ParentModels():
    """ class containing fuctionalities for performing Parent related actions"""
    def __init__(self):
        self.models = BaseModels()

    def save_new_parent(self, data):
        """ Add a new user to the database """
        parent = Parent.query.filter_by(email=data['email']).first()
        if not parent:
            new_parent = Parent(
                first_name=data['first_name'],
                last_name = data['last_name'],
                email=data['email']
                )
            self.models.save_changes(new_parent)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return response_object, 409
