from flask_socketio import SocketIO

# socketio = SocketIO()
socketio = SocketIO(engineio_logger=True, ping_timeout=5, ping_interval=5)