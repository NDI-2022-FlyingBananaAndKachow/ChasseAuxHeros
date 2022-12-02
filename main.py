from flask import Flask, render_template, request, abort, redirect
import json
from random import shuffle

from markupsafe import escape

# Contient l'instance du serveur
app = Flask(__name__, template_folder="templates/", static_folder='static/')

# Charge les données du json
with open("data.json", "r", encoding="utf-8") as f:
	data = json.load(f)


# Sert à tester si le numéro de map est valide
is_map_valid = lambda map_id: 0 < map_id < 5


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
def question(level_id: int, question_id: int, failed: bool = False):
	"""
	Contient et renvoie la question demandée.
	:param level_id: Prend l'ID du niveau (de 1 à 3)
	:param question_id: Prend l'ID de la question (0 à 9).
	"""
	if is_map_valid(level_id) and 0 <= question_id <= len(data[str(level_id)]):
		# On récupère la question
		question = data[str(level_id)][question_id]["question"]

		# On récupère chaque la liste des réponses
		answers = data[str(level_id)][question_id]["answers"]

		# Crée une portée aléatoire d'IDs de réponses
		answer_ids = [i for i in range(4)]
		shuffle(answer_ids)

		# Fait le rendu du template
		return render_template(
			"question.html",
			level_id=level_id,
			question_id=question_id,
			question=question,
			answers=answers,
			failed=failed,
			answer_ids=answer_ids
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
	if is_map_valid(level_id) and 0 <= question_id <= len(data[str(level_id)]):
		# On récupère le texte après-réponse
		after_answer_text = data[str(level_id)][question_id]["after_answer_message"]

		# Fait le rendu du template
		return render_template(
			"reponse.html",
			level_id=level_id,
			question_id=question_id,
			reponse=after_answer_text
		)
	else:
		abort(403)


@app.route('/easter_eggs_random_1021455455155151')
def easter_eggs():
	return 'FDP'


@app.route('/resultat/<int:level_id>/<int:question_id>/<int:answer_id>')
def resultat(level_id: int, question_id: int, answer_id: int):
	"""
	Contient et renvoie la réponse à la question demandée.
	:param level_id: Prend l'ID du niveau (de 1 à 3)
	:param question_id: Prend l'ID de la question (0 à 9).
	:param answer_id: Prend l'ID de la réponse en paramètre.
	"""
	if is_map_valid(level_id) and 0 <= question_id <= len(data[str(level_id)]):
		# Récupère la question
		question_var = data[str(level_id)][question_id]

		# Récupère la question correcte
		valid_answer_id = question_var["correct_answer"]

		# Si la réponse est correcte, on renvoie vers la page de résultat
		if answer_id == valid_answer_id:
			return render_template(
				"reponse.html",
				level_id=level_id,
				question_id=question_id,
				reponse=question_var["after_answer_message"]
			)
		else:
			return question(level_id, question_id, True)
	else:
		abort(403)


if __name__ == '__main__':
	app.debug = True
	app.run()