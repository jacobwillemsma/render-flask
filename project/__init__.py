from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Config
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Blueprints
from project.users.views import users_blueprint
from project.items.views import items_blueprint

# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(items_blueprint)
