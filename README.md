clone repo  
create directory ~/instance/
create /instance/flask.cfg
```
import os

# grab the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

# Update later by using a random number generator and moving
SECRET_KEY = 'secret_key'
WTF_CSRF_ENABLED = True
DEBUG = True

# SQLAlchemy
SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db'
```
create db  
```
export FLASK_APP=run.py
export FLASK_DEBUG=True
flask db init
flask db migrate
flask db upgrade
```
start flask
```
flask run
```
# Render Flask Boilerplate
