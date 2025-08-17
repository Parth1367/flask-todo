from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.todo_db

@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    data = request.get_json()
    item_name = data.get('itemName')
    item_description = data.get('itemDescription')
    if not item_name or not item_description:
        return jsonify({'error': 'Missing itemName or itemDescription'}), 400
    db.todo_items.insert_one({'itemName': item_name, 'itemDescription': item_description})
    return jsonify({'message': 'Item submitted successfully'}), 201
