from flask import Flask, jsonify, request

app = Flask(__name__)

events = [
    { 'date': '2023-04-10', 'time':'14:31:23', 'camera':'prototype', 'location':'sw gate', 'image':'test0', },
    { 'date': '2023-04-10', 'time':'13:30:56', 'camera':'prototype', 'location':'sw gate', 'image':'test1', },
    { 'date': '2023-04-10', 'time':'12:20:23', 'camera':'prototype', 'location':'sw gate', 'image':'test2', },
    { 'date': '2023-04-10', 'time':'11:30:15', 'camera':'prototype', 'location':'sw gate', 'image':'test3', },
    { 'date': '2023-04-10', 'time':'10:30:46', 'camera':'prototype', 'location':'sw gate', 'image':'test4', },
    { 'date': '2023-04-10', 'time':'09:31:25', 'camera':'prototype', 'location':'sw gate', 'image':'test5', },
    { 'date': '2023-04-10', 'time':'09:30:59', 'camera':'prototype', 'location':'sw gate', 'image':'test6', },
    { 'date': '2023-04-10', 'time':'08:20:22', 'camera':'prototype', 'location':'sw gate', 'image':'test7', },
    { 'date': '2023-04-10', 'time':'07:30:10', 'camera':'prototype', 'location':'sw gate', 'image':'test8', },
    { 'date': '2023-04-10', 'time':'06:30:11', 'camera':'prototype', 'location':'sw gate', 'image':'test9', }
]

@app.route("/events")
def get_events():
    return jsonify(events)

@app.route('/events', methods=['POST'])
def add_income():
    events.append(request.get_json())
    return '', 204

if __name__ == "__main__" :
    app.run