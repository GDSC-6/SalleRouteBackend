from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from data.map_data import map_data
from src.pathfinding import dijkstra

app = Flask(__name__)
CORS(app)

rooms = map_data["rooms"]

@app.route("/api/rooms", methods=["GET"])
def get_rooms():
    return jsonify(rooms)

@app.route("/api/rooms/<room_id>", methods=["GET"])
def get_room(room_id):
    for room in rooms:
        if room["id"] == room_id:
            return jsonify(room)
    abort(404, description="Room with specified ID not found")

@app.route("/api/route", methods=["POST"])
def route():
    data = request.get_json()
    start = data.get("start")
    end = data.get("end")

    if not start or not end:
        abort(400, description="Start and end nodes are required")

    nodes = map_data["nodes"]
    edges = map_data["edges"]

    # Call the dijkstra function from pathfinding.py
    path = dijkstra(start, end, nodes, edges)

    return jsonify({"path": path})

if __name__ == "__main__":
    app.run(debug=True)