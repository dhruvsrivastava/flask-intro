import sqlite3

with sqlite3.connect("sample.db") as connection:
#creates database if it does not exist
	c = connection.cursor()
	c.execute('DROP TABLE posts')
	c.execute('CREATE TABLE posts(title TEXT , description TEXT) ')
	c.execute('INSERT INTO posts VALUES("Good" , "I\'m good")')
	c.execute('INSERT INTO posts VALUES("Well" , "I\'m well")')

	c.execute('DROP TABLE codes')
	c.execute('CREATE TABLE codes(id INTEGER , code TEXT) ')
	codeString = 'print "Hello world" '
	c.execute("INSERT INTO codes VALUES (1, ?)", (codeString,))
	codeString = 'print "Second code" '
	c.execute("INSERT INTO codes VALUES (2, ?)", (codeString,))
