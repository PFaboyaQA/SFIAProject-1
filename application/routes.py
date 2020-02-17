from flask import render_template, url_for, redirect
from application import app, db
from applications.forms import AddGenreForm, AddGameForm, PlayersForm
from applications.models import Players, Genres, Games

@app.route('/')
@app.route('/home')
def home():
	playerData = Players.query.all()
	return render_template('home.html', title='Home', players=playerData)

@app.route('/genre', methods=['GET', 'POST'])
def genre():
	if add_genre = AddGenreForm()
		add_genre_to_db = Genre(
				name = add_genre.name.data
				)
		db.session.add(add_genre_to_db)
		db.session.commit()
		return redirect(url_for('genre'))
	else:
		print(add_genre.errors)
		genreData = Genres.query.all()
		return render_template('genre.html', title='Genre', genres=genreData, form=add.genre)

@app.route('/game', methods={'GET', 'POST')
def game():
	gameData = Games.query.all()
	return render_template('game.html', title='Games', games=gameData)

@app.route('/register', methods=('GET', 'POST')
def post():
	form = PlayersForm
	if form.validate_on_submit():
		playerData = players(
			first_name = form.first_name.data
			last_name = form.last_name.data
			fav_genre_id = form.fav_genre_id.data
			email = form.email.data
			fav_game_id = form.fav_game_id.data
			)
		db.session.add(playerData)
		db.session.commit()
		return redirect(url_for('home'))
	else:
		print(form.errors)

	return render_template('post.html', title='post', form=form)
