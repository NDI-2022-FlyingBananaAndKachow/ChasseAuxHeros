from flask import Flask, render_template, request, abort, redirect
import json

from markupsafe import escape

# Contient l'instance du serveur
app = Flask(__name__, template_folder="templates/", static_folder='static/')

# Charge les données du json
with open("data.json", "r", encoding="utf-8") as f:
	data = json.load(f)


# Sert à tester si le numéro de map est valide
is_map_valid = lambda map_id: 0 < map_id < 5
is_question_valid = lambda question_id: 0 < question_id < 10


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
	if is_map_valid(level_id):
		if level_id == 3:
			return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
		if level_id > 3:
			level_id -= 1
		return render_template("level.html", level_id=level_id)
	else:
		abort(403)


@app.route('/questions/<int:level_id>/<int:question_id>')
def question(level_id: int, question_id: int):
	"""
	Contient et renvoie la question demandée.
	:param level_id: Prend l'ID du niveau (de 1 à 3)
	:param question_id: Prend l'ID de la question (0 à 9).
	"""
	if is_map_valid(level_id) and is_question_valid(question_id):
		# On récupère la question
		question = data[str(level_id)][question_id]["question"]

		# On récupère chaque la liste des réponses
		answers = data[str(level_id)][question_id]["answers"]

		# Fait le rendu du template
		return render_template(
			"question.html",
			level_id=level_id,
			question_id=question_id,
			question=question,
			answers=answers
		)
	else:
		abort(403)


@app.route('/reponse/<int:level_id>/<int:question_id>')
def reponse(level_id: int, question_id: int):
	"""
	Contient et renvoie la réponse à la question demandée.
	:param level_id: Prend l'ID du niveau (de 1 à 3)
	:param question_id: Prend l'ID de la question (0 à 5).
	"""
	if is_map_valid(level_id) and is_question_valid(question_id):
		return render_template("reponse.html", level_id=level_id, question_id=question_id)
	else:
		abort(403)


@app.route('/easter_eggs_random_1021455455155151')
def easter_eggs():
	return 'FPD'


@app.post('/resultat/<int:level_id>/<int:question_id>')
def resultat(level_id: int, question_id: int):
	"""
	Contient et renvoie la réponse à la question demandée.
	:param level_id: Prend l'ID du niveau (de 1 à 3)
	:param question_id: Prend l'ID de la question (0 à 9).
	"""
	pass


if __name__ == '__main__':
	app.debug = True
	app.run()