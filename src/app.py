from pathlib import Path
from flask import Flask, render_template, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from models import db
from models.Account import Account
from helpers import generateAccountGraph
from api import BrokerAPI
from apscheduler.schedulers.background import BackgroundScheduler

import atexit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

@app.route('/api/data')
def get_data():
    return jsonify({
        'data': 'Hello World!'
    })

@app.route('/')
def index():
    account_history_data = Account.getHistory()
    
    graphJSON = generateAccountGraph(account_history_data)

    return render_template('index.html' , graphJSON=graphJSON)

scheduler = BackgroundScheduler()
broker_api_instance = BrokerAPI()


scheduler.add_job(func=broker_api_instance.get_account, trigger='interval', minutes=5)
scheduler.add_job(func=broker_api_instance.get_portfolio, trigger='interval', minutes=5)

scheduler.start()
atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run(debug=True)