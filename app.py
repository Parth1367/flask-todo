from flask import Flask, jsonify
import json

app = Flask(__name__)

def load_data():
    with open('data.json') as f:
        return json.load(f)

@app.route('/api', methods=['GET'])
def api():
    data = load_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
