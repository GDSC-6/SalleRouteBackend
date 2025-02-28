from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open("rooms.json") as f:
    rooms = json.load(f)

@app.route("/api/rooms", methods=["GET"])
def get_rooms():
    return jsonify(rooms)

@app.route("/api/rooms/<room_id>", methods=["GET"])
def get_room(room_id):
    for room in rooms:
        if room["id"] == room_id:
            return jsonify(room)
    abort(404, description="Room with specified ID not found")

if __name__ == "__main__":
    app.run(debug=True)