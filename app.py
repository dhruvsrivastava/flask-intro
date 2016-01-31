# import the Flask class from the flask module
from flask import Flask, render_template
from flask import redirect , request , url_for

<<<<<<< HEAD
from flask import g
#global flask object

import sqlite3

app = Flask(__name__)
app.database = 'sample.db'
=======
app = Flask(__name__)
>>>>>>> 3971fc5038429889052693e32cb6fa0932aa39f2

@app.route('/')
def home():
    return "Hello, World!"  # return a string

<<<<<<< HEAD
@app.route('/display')
def display():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('posts.html' , posts = posts)

=======
>>>>>>> 3971fc5038429889052693e32cb6fa0932aa39f2
@app.route('/login' , methods = ["GET" , "POST"])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = "Username/Password Incorrect"
		else :
			# print "login successful"
			return redirect(url_for('home'))
	return render_template('login.html' , error = error)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

<<<<<<< HEAD

def connect_db():
	return sqlite3.connect(app.database)

=======
>>>>>>> 3971fc5038429889052693e32cb6fa0932aa39f2
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug = True)
