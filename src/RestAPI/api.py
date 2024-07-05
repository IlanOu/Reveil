from flask import Flask, jsonify, request
import json

app = Flask(__name__)

store = {}
with open("./assets/alarm_config.json", 'r') as f:
    store = json.load(f)

@app.route('/')
def get_root():
    return "Connected", 200

@app.route('/alarms')
def get_alarms():
    return jsonify(store)


@app.route('/alarms', methods=['POST'])
def add_alarm():
    print(request.get_json())
    return '', 204

def startAPI():
    app.run()
    
if __name__ == "__main__":
    app.run()