# import the Flask class from the flask module
from flask import Flask, render_template
from flask import redirect , request , url_for
from bs4 import BeautifulSoup
from urllib2 import urlopen

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

@app.route('/404')
def Error_404():
    return render_template('404.html')

@app.route('/users/<username>')
def user_profile(username):
    if username != "dhruv":
        return redirect('/404') 
    return "Hello %s" %username

@app.route('/contest_list')
def contest_list():
    url=urlopen("http://clist.by/")
    soup = BeautifulSoup(url)
    x = []
    y = []
    for link in soup.find_all('div' , class_ = "contest-title"):
        x.append(link.a["title"])
        y.append(link.a["href"])
        # print link.a["title"]
        # print link.a["href"]
    return render_template("clist.html" , cnames = x , clinks = y , item = x[0])

@app.route('/submissions')
def submissions():
	g.db = connect_db()
	cur = g.db.execute('select * from codes')
	codes = [dict(id = row[0] , code = row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template('submissions.html' , codes = codes)

@app.route('/posts')
def posts():
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
