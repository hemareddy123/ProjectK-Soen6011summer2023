# This is a sample Python script.
import request

import hashlib
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database information and config.
db = mysql.connector.connect(host = "localhost",user = "root", password="root@1234", database="loginmodule")

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods = ['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # checking if a user exist already.
    cursor = db.cursor()
    cursor.execute('SELECT * FROM useraccounts WHERE emailid = %s AND password=%s',(email,password))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return "Login Successful"
    else:
        return "Login failed. Invalid user credentials."

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = db.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not request.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not request.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO useraccounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)



if __name__ == '__main__':
    app.run()
