from flask import Flask, render_template, request

from markupsafe import escape

app = Flask(__name__, template_folder="templates/", static_folder='static/')

@app.route('/')
def index():
	return "Hello world!"


if __name__ == '__main__':
	app.debug = True
	app.run()