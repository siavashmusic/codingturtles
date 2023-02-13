#import MySQLdb
from flask import Flask
#from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# from application.models import User


app = Flask(__name__)
DB_NAME = "database.db"
db = SQLAlchemy()

#db = MySQL(app)


def create_app():

    app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
    #app.config['SQLALCHEMY_DATABASE_URI'] = F"sqlite:///{DB_NAME}"

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://u4bc1v5jfnkk79:p81fb17c0b8d125dc51939e2d40947cbaa365ce2341d3c18101558e4651cb8861@ec2-54-89-81-44.compute-1.amazonaws.com:5432/d6fgdjsmqlbk4f"
    # app.config['MYSQL_HOST'] = 'localhost'
    # app.config['MYSQL_USER'] = 'root'
    # app.config['MYSQL_PASSWORD'] = '1359slSL@'
    # app.config['MYSQL_DB'] = 'flask'
    db.init_app(app)


# REGISTER OUR ROUTS
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Mentor

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    with app.app_context():
        db.create_all()
    return app


def create_database(app):
    if not path.exists('codingturtles/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Created Database!")


# from application import routes

