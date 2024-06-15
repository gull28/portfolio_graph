from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db

class Position(db.Model):
    __tablename__ = 'positions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    average_price = db.Column(db.Float, nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    fill_date = db.Column(db.DateTime, nullable=False)
    max_buy_price = db.Column(db.Float, nullable=False)
    max_sell_price = db.Column(db.Float, nullable=False)
    pie_quant = db.Column(db.Float, nullable=False)
    quant = db.Column(db.Float, nullable=False)
    ticker = db.Column(db.String(5), nullable=False)

    def __init__(self, average_price, current_price, fill_date, max_buy_price, max_sell_price, pie_quant, quant, ticker):
        self.average_price = average_price
        self.current_price = current_price
        self.fill_date = fill_date
        self.max_buy_price = max_buy_price
        self.max_sell_price = max_sell_price
        self.pie_quant = pie_quant
        self.quant = quant
        self.ticker = ticker
    
    def create(self):
        if not Position.query.filter_by(ticker=self.ticker).first():
            db.session.add(self)
            db.session.commit()
        else:
            self.update()
    
    def update(self):
        db.session.commit()

    @staticmethod
    def getPositions():
        return Position.query.all()
    
    @staticmethod
    def getPosition(ticker):
        return Position.query.filter_by(ticker=ticker).first()

