from pathlib import Path
from dotenv import load_dotenv
import requests
import os

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
        response.raise_for_status() 

        data = response.json()

        # todo: pass to model
        return data

    def get_account(self):
        url = "https://live.trading212.com/api/v0/account"

        response = requests.get(url, headers=self.headers)
        response.raise_for_status() 

        data = response.json()

        # todo: pass to model
        return data

