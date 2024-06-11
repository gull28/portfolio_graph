from flask import Flask, render_template, jsonify
import plotly
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import json

app = Flask(__name__)

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
