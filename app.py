from flask import Flask, request, jsonify
import json
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://localhost:27017'

mongo = PyMongo(app)
db = mongo.db

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Welcome to the todo list server's main page"

if __name__ == '__main__':
    # Default port is 5000 on local host
    app.run()