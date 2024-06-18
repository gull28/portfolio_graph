from pathlib import Path
from flask import Flask, render_template, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from models.Account import Account
from models.Position import Position
from helpers import generateAccountGraph
from api import BrokerAPI
from apscheduler.schedulers.background import BackgroundScheduler
from db import create_app, db
import atexit

app = create_app()

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
    positions = Position.getAll()

    return render_template('index.html', graphJSON=graphJSON, positions=positions)

scheduler = BackgroundScheduler()
broker_api_instance = BrokerAPI()


scheduler.add_job(func=broker_api_instance.get_account, trigger='interval', minutes=15)
scheduler.add_job(func=broker_api_instance.get_portfolio, trigger='interval', minutes=2)

scheduler.start()
atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run(debug=True)