from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from db import db, create_app

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    blocked = db.Column(db.Float, nullable=False)
    free = db.Column(db.Float, nullable=False)
    invested = db.Column(db.Float, nullable=False)
    pie_cash = db.Column(db.Float, nullable=False)
    result = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, blocked=None, free=None, invested=None, pie_cash=None, result=None, total=None):
        self.blocked = 0.0 if blocked is None else blocked
        self.free = 0.0 if free is None else free
        self.invested = 0.0 if invested is None else invested
        self.pie_cash = 0.0 if pie_cash is None else pie_cash
        self.result = 0.0 if result is None else result
        self.total = 0.0 if total is None else total
        self.timestamp = datetime.now()

    def create(self):
        app = create_app()
        with app.app_context():
            db.session.add(self)
            db.session.commit()

    @staticmethod
    def getLatestAccount():
        return Account.query.order_by(Account.id.desc()).first()

    @staticmethod
    def getHistory():
        return Account.query.all()
