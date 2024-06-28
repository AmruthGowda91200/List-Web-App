from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ghjkldklfnkld ekfdklsfslkf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prfix="/")
    app.register_blueprint(auth, url_prfix="/")

    return app