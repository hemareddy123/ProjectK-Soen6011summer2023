from socket_cr import socketio
from flask_socketio import emit
from Models.User import User
from Models.Student import Student

# connecting to a socket, which allows multiple different connections.
@socketio.on("connect")
def handle_connect():
    print('client connected')

# socket recieves the new message from the client and response from the
# server the client and storing the message into database
@socketio.on("new_message")
def handle_message(text,initater,empId,studId):
    print("text : " + text)
    username = ''
    if initater == 'employer':
        username = User.get_user_by_id(empId).username
    else:
        username = Student.get_user_by_id(studId).username

    emit("chat",{"message":text,"initater": initater,"username":username,"empId":empId,"studId":studId},broadcast=True)
    socketio.sleep(0)

# disconnecting the socket from the server side
@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')