from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from instance.config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

from .api.v1 import version_one as v1

def create_app(config_name):
    app = Flask(__name__)
    print(config_name)
    app.register_blueprint(v1)
    app.config.from_object(config_by_name['dev'])
    app.app_context().push()
    manager = Manager(app)
    migrate = Migrate(app, db)
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app


from app.utils.database.schemas import Admin, Parent, Student, Semister, Course, Unit, Result, Fee
