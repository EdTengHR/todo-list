from flask import Flask, request, jsonify
import json
from flask_pymongo import PyMongo
import os
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://localhost:27017/flaskdb'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

mongo = PyMongo(app)
db = mongo.db

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Welcome to the todo list server's main page"

@app.route('/list', methods=['GET'])
def show():
    toDoList = db.todo.find()

    item = {}
    data = []
    for todo in toDoList:
        item = {
            '_id': str(todo['_id']),
            'id' : todo['id'],
            'todo': todo['todo'],
            'marked': todo['marked']
        }

        data.append(item)

    return jsonify(
        data=data
    )

@app.route('/add', methods=['GET'])
def add():
    data_id = request.args.get('id')
    data = request.args.get('todo')

    toAdd = {
        'id': data_id,
        'todo': data,
        'marked': False,
    }

    db.todo.insert_one(toAdd)

    return jsonify(
        status=True,
        message='Item ' + data + ' added successfully!'
    ), 201

@app.route('/delete', methods=['GET'])
def delete():
    _id = request.args.get('_id')

    toDelete = {
        '_id': ObjectId(_id)
    }

    result = db.todo.delete_one(toDelete)

    return jsonify(
        status=True,
        message=str(result.deleted_count) + ' document deleted'
    ), 200

@app.route('/mark-complete', methods=['GET'])
def markComplete():
    _id = request.args.get('_id')

    toMark = {
        '_id': ObjectId(_id)
    }

    result = db.todo.update_one(toMark, { "$set": { "marked": True } })

    return jsonify(
        status=True,
        message=str(result.modified_count) + ' documents modified'
    ), 200

if __name__ == '__main__':
    # Default port is 5000 on local host
    app.run(host='0.0.0.0', port=5000)