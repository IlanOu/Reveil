from flask import Flask, jsonify, request
import json

app = Flask(__name__)

store = {}
with open("./assets/store.json", 'r') as f:
    store = json.load(f)

# ---------------------------------------------------------------------------- #
#                                  GET METHODS                                 #
# ---------------------------------------------------------------------------- #
@app.route('/api/', methods=['GET'])
def get_root():
    return "Connected", 200

@app.route('/api/alarms', methods=['GET'])
def get_alarms():
    return jsonify(store)


# ---------------------------------------------------------------------------- #
#                                 POST METHODS                                 #
# ---------------------------------------------------------------------------- #
# For add data
@app.route('/api/alarms', methods=['POST'])
def add_alarm():
    print(request.get_json())
    return '', 204

@app.route('/api/days', methods=['POST'])
def add_days():
    print(request.get_json())
    return '', 204

@app.route('/api/actions', methods=['POST'])
def add_actions():
    print(request.get_json())
    return '', 204
# ---------------------------------------------------------------------------- #
#                                  PUT METHODS                                 #
# ---------------------------------------------------------------------------- #
# For replace data
@app.route('/api/name', methods=['PUT'])
def update_name():
    print(request.get_json())
    return '', 204

@app.route('/api/ringonce', methods=['PUT'])
def update_ringonce():
    print(request.get_json())
    return '', 204

@app.route('/api/isactivated', methods=['PUT'])
def update_isactivated():
    print(request.get_json())
    return '', 204

@app.route('/api/days', methods=['PUT'])
def update_days():
    print(request.get_json())
    return '', 204

@app.route('/api/time', methods=['PUT'])
def update_time():
    print(request.get_json())
    return '', 204

@app.route('/api/actions', methods=['PUT'])
def update_actions():
    print(request.get_json())
    return '', 204

# ---------------------------------------------------------------------------- #
#                                DELETE METHODS                                #
# ---------------------------------------------------------------------------- #
@app.route('/api/clock', methods=['DELETE'])
def delete_clock():
    print(request.get_json())
    return '', 204

def startAPI():
    app.run()
    
if __name__ == "__main__":
    app.run()