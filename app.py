from flask import Flask, request, jsonify
import json
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://localhost:27017/flaskdb'


mongo = PyMongo(app)
db = mongo.db

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Welcome to the todo list server's main page"

@app.route('/list', methods=['GET'])
def show():
    toDoList = db.todo.find()

    # item = {}
    # data = []
    # for todo in toDoList:
    #     item = {
    #         'id': str(todo['_id']),
    #         'todo': todo['todo'],
    #         'marked': todo['marked']
    #     }

    #     data.append(item)

    # return jsonify(
    #     status=True,
    #     data=data
    # )

    return jsonify([todo for todo in toDoList])

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        data_id = request.args.get('id')
        data = request.args.get('todo')

        toAdd = {
            '_id': data_id,
            'todo': data,
            'marked': False,
        }

        db.todo.insert_one(toAdd)

        return jsonify(
            status=True,
            message='Item ' + data + ' added successfully!'
        ), 201

    else: 
        data = request.get_json(force=True)

        toAdd = {
            'todo': data['todo'],
            'marked': False,
        }

        db.todo.insert_one(toAdd)

        return jsonify(
            status=True,
            message='Item ' + data['todo'] + ' added successfully!'
        ), 201

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    if request.method == 'GET':
        data = request.args.get('id')

        toDelete = {
            '_id': data
        }

        db.todo.delete_one(toDelete)

        return jsonify(
            status=True,
            message='Item ' + data + ' deleted successfully!'
        ), 200

    else:
        data = request.get_json(force=True)

        toDelete = {
            '_id': data['id']
        }

        db.todo.delete_one(toDelete)

        return jsonify(
            status=True,
            message='Item ' + data['id'] + ' deleted successfully!'
        ), 200

@app.route('/mark-complete', methods=['GET', 'PUT'])
def markComplete():
    if request.method == 'GET':
        data = request.args.get('id')

        toMark = {
            '_id': data
        }

        db.todo.update_one(toMark, { "$set": { "marked": "true" } })

        return jsonify(
            status=True,
            message='Item ' + data + ' marked as completed! (GET)'
        ), 200

    else:
        data = request.get_json(force=True)

        toMark = {
            '_id': data['id']
        }

        db.todo.update_one(toMark, { "$set": { "marked": True } })

        return jsonify(
            status=True,
            message='Item ' + data['id'] + ' marked as completed!'
        ), 200

if __name__ == '__main__':
    # Default port is 5000 on local host
    app.run(host='0.0.0.0', port=5000)