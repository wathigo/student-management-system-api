
""" local imports """
from app import db


class BaseModels():
    """ A base class containing common fuctionalities"""

    def save_changes(self, data):
        """ Method to store changes to the database"""
        db.session.add(data)
        db.session.commit()
