from flask import Flask, render_template, request

from markupsafe import escape

app = Flask(__name__, template_folder="templates/", static_folder='static/')


@app.route('/')
def index():
	"""
	Page d'accueil.
	"""
	return render_template("accueil.html")


@app.route('/levels/<int:level_id>')
def level(level_id: int):
	"""
	Contient et renvoie les maps et niveaux.
	:param level_id: Prend le l'ID du niveau (de 1 à 3).
	"""
	return render_template("level.html", level_id=level_id)


@app.route('/questions/<int:level_id>/<int:question_id>')
def question(level_id: int, question_id: int):
	"""
	Contient et renvoie la question demandée.
	:param level_id: Prend l'ID du niveau (de 1 à 3)
	:param question_id: Prend l'ID de la question (0 à 9).
	"""
	return render_template("question.html", level_id=level_id, question_id=question_id)


@app.route('/reponse/<int:level_id>/<int:question_id>')
def reponse(level_id: int, question_id: int):
	"""
	Contient et renvoie la réponse à la question demandée.
	:param level_id: Prend l'ID du niveau (de 1 à 3)
	:param question_id: Prend l'ID de la question (0 à 9).
	"""
	return render_template("reponse.html", level_id=level_id, question_id=question_id)


if __name__ == '__main__':
	app.debug = True
	app.run()