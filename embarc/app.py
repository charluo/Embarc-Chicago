from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

socketio = SocketIO(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['WTF_CSRF_SECRET_KEY'] = 'blueturtle'
app.secret_key = 'greenelephant'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

redis = redis.StrictRedis(host='localhost', port=6379, db=0)
