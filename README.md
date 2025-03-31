# SalleRouteBackend

## Overview
SalleRouteBackend is a Flask-based backend application designed to provide room information and route finding within a building. The application uses Dijkstra's algorithm to find the shortest path between rooms.

## Features
- Retrieve a list of rooms
- Retrieve details of a specific room by ID
- Find the shortest route between two rooms

## Project Structure
- `data/map_data.py`: Contains the map data including rooms, nodes, and edges.
- `data/GraphObjects.py`: Defines the `Node` and `Edge` classes.
- `app.py`: Main Flask application with API endpoints.
- `src/pathfinding.py`: Contains the implementation of Dijkstra's algorithm.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/SalleRouteBackend.git
    cd SalleRouteBackend
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Access the API endpoints:
    - Get all rooms: `GET /api/rooms`
    - Get a specific room by ID: `GET /api/rooms/<room_id>`
    - Find the shortest route between two rooms: `POST /api/route`
        - Request body example:
          ```json
          {
            "start": "start",
            "end": "831"
          }
          ```

## API Endpoints
- **GET /api/rooms**: Returns a list of all rooms.
    - **Example Request**:
      ```sh
      curl -X GET http://127.0.0.1:5000/api/rooms
      ```
    - **Example Response**:
      ```json
      [
        {"id": "831", "name": "Room 831", "category": "room", "x": 113, "y": 116},
        {"id": "833", "name": "Room 833", "category": "room", "x": 180, "y": 116},
        {"id": "835", "name": "Room 833", "category": "room", "x": 237, "y": 116},
        {"id": "837", "name": "Room 833", "category": "room", "x": 257, "y": 116},
        {"id": "start", "name": "Entrance", "category": "start", "x": 369, "y": 252}
      ]
      ```

- **GET /api/rooms/<room_id>**: Returns details of a specific room by ID.
    - **Example Request**:
      ```sh
      curl -X GET http://127.0.0.1:5000/api/rooms/831
      ```
    - **Example Response**:
      ```json
      {
        "id": "831",
        "name": "Room 831",
        "category": "room",
        "x": 113,
        "y": 116
      }
      ```

- **POST /api/route**: Finds the shortest route between two rooms. Requires `start` and `end` in the request body.
    - **Example Request**:
      ```sh
      curl -X POST http://127.0.0.1:5000/api/route -H "Content-Type: application/json" -d '{"start": "start", "end": "831"}'
      ```
    - **Example Response**:
      ```json
      {
        "path": ["start", "837", "831"]
      }
      ```

## License
This project is licensed under the MIT License.