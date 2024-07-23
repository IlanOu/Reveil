from flask import Flask, jsonify, request
from apiVerificationMethods import *
import json
import uuid
app = Flask(__name__)

store = {}
with open("./assets/store.json", 'r') as f:
    store = json.load(f)

# ---------------------------------------------------------------------------- #
#                                  GET METHODS                                 #
# ---------------------------------------------------------------------------- #
@app.route('/api/', methods=['GET'])
def get_root():
    # TODO connect webhook
    return "Connected", 200

@app.route('/api/alarms', methods=['GET'])
def get_alarms():
    return jsonify(store["alarms"])


# ---------------------------------------------------------------------------- #
#                                 POST METHODS                                 #
# ---------------------------------------------------------------------------- #
# For add data
@app.route('/api/alarms', methods=['POST'])
def add_alarm():
    data = request.get_json()
    if add_alarm_verification(data):
        data["id"] = uuid.uuid4()
        return 200
    else:
        return data, 400

@app.route('/api/days', methods=['POST'])
def add_days():
    data = request.get_json()
    if add_days_verification(data):
        return 200
    else:
        return data, 400

@app.route('/api/actions', methods=['POST'])
def add_actions():
    data = request.get_json()
    if add_actions_verification(data):
        return 200
    else:
        return data, 400
# ---------------------------------------------------------------------------- #
#                                  PUT METHODS                                 #
# ---------------------------------------------------------------------------- #
# For replace data
@app.route('/api/name', methods=['PUT'])
def update_name():
    data = request.get_json()
    if update_name_verification(data):
        return 200
    else:
        return data, 400

@app.route('/api/ringonce', methods=['PUT'])
def update_ringonce():
    data = request.get_json()
    if update_ringonce_verification(data):
        return 200
    else:
        return data, 400

@app.route('/api/isactivated', methods=['PUT'])
def update_isactivated():
    data = request.get_json()
    if update_isactivated_verification(data):
        return 200
    else:
        return data, 400
    
@app.route('/api/days', methods=['PUT'])
def update_days():
    data = request.get_json()
    if update_days_verification(data):
        return 200
    else:
        return data, 400

@app.route('/api/time', methods=['PUT'])
def update_time():
    data = request.get_json()
    if update_time_verification(data):
        return 200
    else:
        return data, 400

@app.route('/api/actions', methods=['PUT'])
def update_actions():
    data = request.get_json()
    if update_actions_verification(data):
        return 200
    else:
        return data, 400

# ---------------------------------------------------------------------------- #
#                                DELETE METHODS                                #
# ---------------------------------------------------------------------------- #
@app.route('/api/clock', methods=['DELETE'])
def delete_clock():
    data = request.get_json()
    if delete_clock_verification(data):
        return 200
    else:
        return data, 400

def startAPI():
    app.run()
    
if __name__ == "__main__":
    app.run()