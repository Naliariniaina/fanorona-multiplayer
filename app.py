from flask import Flask, request
from flask_socketio import SocketIO, join_room, emit
import uuid

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

waiting_player = None

@socketio.on("join_game")
def handle_join():
    global waiting_player

    if waiting_player is None:
        waiting_player = request.sid
        emit("status", "Miandry mpilalao hafa...")
    else:
        room_id = str(uuid.uuid4())
        join_room(room_id)
        emit("start_game", {"room": room_id}, room=room_id)
        waiting_player = None

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=10000)
