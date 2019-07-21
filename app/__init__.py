from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, MigrateCommand

from instance.config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

from .api.v1 import version_one as v1

def create_app(name_config):
    app = Flask(__name__)
    print(name_config)
    app.register_blueprint(v1)
    app.config.from_object(config_by_name["dev"])
    app.app_context().push()
    migrate = Migrate(app, db)
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app


from app.utils.database.schemas import Admin, Parent, Student, Semister, Course, Unit, Result, Fee
