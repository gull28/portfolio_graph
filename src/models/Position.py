from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from db import db, create_app

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
    ticker = db.Column(db.String(20), nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __init__(self, average_price, current_price, fill_date, max_buy_price, max_sell_price, pie_quant, quant, ticker):
        self.average_price = average_price
        self.current_price = current_price
        self.fill_date = datetime.fromisoformat(fill_date) if isinstance(fill_date, str) else fill_date
        self.max_buy_price = max_buy_price
        self.max_sell_price = max_sell_price
        self.pie_quant = pie_quant
        self.quant = quant
        self.ticker = ticker
        self.total = self.quant * self.current_price
    
    def create(self):
        app = create_app()

        with app.app_context():
            db.session.add(self)
            db.session.commit()
    
    @staticmethod
    def getAll():
        return Position.query.order_by(Position.total.desc()).all()
    
    @staticmethod
    def getPosition(ticker):
        return Position.query.filter_by(ticker=ticker).first()

