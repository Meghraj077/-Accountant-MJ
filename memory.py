from flask import Flask, request, jsonify
from memory import remember, recall

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Accountant-MJ API!"

@app.route('/remember', methods=['POST'])
def save_memory():
    data = request.json
    key = data.get("key")
    value = data.get("value")
    
    if not key or not value:
        return jsonify({"error": "Key और Value दोनों चाहिए!"}), 400
    
    response = remember(key, value)
    return jsonify({"message": response})

@app.route('/recall', methods=['GET'])
def get_memory():
    key = request.args.get("key")
    
    if not key:
        return jsonify({"error": "Key चाहिए!"}), 400
    
    response = recall(key)
    return jsonify({"message": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
