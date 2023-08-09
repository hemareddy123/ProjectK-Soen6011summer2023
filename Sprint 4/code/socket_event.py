from socket_cr import socketio
from flask_socketio import emit

@socketio.on("connect")
def handle_connect():
    print('client connected')

@socketio.on("new_message")
def handle_message(text,initater):
    print("text : " + text)
    emit("chat",{"message":text,"initater": initater},broadcast=True)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')