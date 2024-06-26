from pathlib import Path
from dotenv import load_dotenv
import requests
import os
from models.Position import Position
from models.Account import Account
from db import db, create_app
from sqlalchemy import delete

class BrokerAPI:
    def __init__(self):
        path = Path(__file__).parent
        load_dotenv(dotenv_path=path/'../.env')

        self.api_key = os.getenv("BROKER_API_KEY")
        
        if not self.api_key:
            raise ValueError("BROKER_API_KEY not found in .env file")
        
        self.headers = {"Authorization": self.api_key}

    def get_portfolio(self):
        url = "https://live.trading212.com/api/v0/equity/portfolio"

        response = requests.get(url, headers=self.headers)
        
        if(response.status_code == 429):
            print("Rate limit reached")
            return

        data = response.json()

        app = create_app()

        # for the sake of simplicity
        with app.app_context():
            db.session.query(Position).delete()
            db.session.commit()

        for position in data:
            position_instance = Position(
                average_price=position['averagePrice'],
                current_price=position['currentPrice'],
                fill_date=position['initialFillDate'],
                max_buy_price=position['maxBuy'],
                max_sell_price=position['maxSell'],
                pie_quant=position['pieQuantity'],
                quant=position['quantity'],
                ticker=position['ticker']
            )

            position_instance.create()

    def get_account(self):
        url = "https://live.trading212.com/api/v0/equity/account/cash"

        response = requests.get(url, headers=self.headers)
        response.raise_for_status() 

        data = response.json()

        account_instance = Account(
            blocked=data['blocked'],
            free=data['free'],
            invested=data['invested'],
            pie_cash=data['pieCash'],
            result=data['result'],
            total=data['total']
        )
        
        account_instance.create()
