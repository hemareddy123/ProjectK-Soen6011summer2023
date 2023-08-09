from flask_socketio import SocketIO

#using socketIO for setting up the connections
socketio = SocketIO(engineio_logger=True, ping_timeout=5, ping_interval=5)