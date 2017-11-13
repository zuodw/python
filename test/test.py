#coding=utf-8

from flask import Flask

app = Flask('__name__')

@app.route('/user/<username>')
def hello_world(username):
	return 'Hello  %s! % (username)'

if __name__ == '__main__':
	app.run(debug=True)