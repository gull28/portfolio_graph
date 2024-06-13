from flask_sqlalchemy import SQLAlchemy
from models import db

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    blocked = db.Column(db.Float, nullable=False)
    free = db.Column(db.Float, nullable=False)
    invested = db.Column(db.Float, nullable=False)
    pie_cash = db.Column(db.Float, nullable=False)
    result = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __init__(self, blocked, free, invested, pie_cash, result, total):
        self.blocked = blocked
        self.free = free
        self.invested = invested
        self.pie_cash = pie_cash
        self.result = result
        self.total = total
    

    def create(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def getLatestAccount(self):
        return Account.query.order_by(Account.id.desc()).first()

    def getHistory(self):
        return Account.query.all()


