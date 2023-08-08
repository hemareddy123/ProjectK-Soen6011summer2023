from socket import socketio

@socketio.on("connect")
def handle_request():
    print('client connected')