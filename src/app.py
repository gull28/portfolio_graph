from pathlib import Path
from flask import Flask, render_template, jsonify
import plotly
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import json
from flask_sqlalchemy import SQLAlchemy
from models import db  
from models.Position import Position
from models.Account import Account

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
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
