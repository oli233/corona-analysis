# import datetime

from flask import Flask, jsonify
from DataDriver.DataDrive import DataDrive

datapool = DataDrive('0.0.0.0', '6379')  # replace your data pool address
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!", 200


@app.route('/api/corona/v1.0/all', methods=['GET'])
def day_update():
    data = datapool.dataoftoday()
    return jsonify(data), 200


@app.route('/api/corona/v1.0/date=<string:date>&id=<string:country_name>', methods=['GET'])
def single_data(date, country_name):
    data = datapool.lookup(date, country_name)
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
