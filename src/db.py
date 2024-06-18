from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app_instance = None
db = SQLAlchemy()

def create_app():
    global app_instance
    if app_instance is None:
        app_instance = Flask(__name__)
        app_instance.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
        app_instance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app_instance.config["SQLALCHEMY_POOL_SIZE"] = 20
        
        db.init_app(app_instance)

        with app_instance.app_context():
            from models.Account import Account
            from models.Position import Position
            db.create_all()

    return app_instance
