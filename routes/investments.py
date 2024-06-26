from flask import Blueprint, request, jsonify
import requests
import os

investments = Blueprint('investments', __name__)

ALPHA_VANTAGE_API_KEY = os.environ.get('VANTAGE_KEY')

@investments.route('/investments', methods=['GET'])
def get_investments():
    # Example: Fetch stock data from Alpha Vantage
    stock_symbol = request.args.get('symbol', 'AAPL')
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@investments.route('/investments/<symbol>', methods=['GET'])
def get_investment_details(symbol):
    # Example: Fetch detailed stock data from Alpha Vantage
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)