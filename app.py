# import the Flask class from the flask module
from flask import Flask, render_template
from flask import redirect , request , url_for

from flask import g
#global flask object

import sqlite3

app = Flask(__name__)
app.database = 'sample.db'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_me')
def about_me():
	return render_template('about_me.html')

@app.route('/display')
def display():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('posts.html' , posts = posts)

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


def connect_db():
	return sqlite3.connect(app.database)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug = True)
