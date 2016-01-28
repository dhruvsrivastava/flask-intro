# import the Flask class from the flask module
from flask import Flask, render_template
from flask import redirect , request , url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"  # return a string

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

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug = True)
