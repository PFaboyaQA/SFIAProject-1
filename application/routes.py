from flask import render_template, url_for, redirect, request
from application import app, db
from application.forms import AddGenreForm, AddGameForm, PlayerForm
from application.models import Players, Genres, Games

@app.route('/')
@app.route('/home')
def home():
	playerData = Players.query.all()
	return render_template('home.html', title='Home', players=playerData)

@app.route('/genre', methods=['GET', 'POST'])
def genre():
        add_genre = AddGenreForm()
        if add_genre.validate_on_submit():
                add_genre_to_db = Genres(
				genre_name = add_genre.genre_name.data
				)
                db.session.add(add_genre_to_db)
                db.session.commit()
                return redirect(url_for('genre'))
        else:
	        print(add_genre.errors)
	        genreData = Genres.query.all()
        return render_template('genre.html', title='Genre', genres=genreData, form=add_genre)

@app.route('/game', methods=['GET', 'POST'])
def game():
        add_game = AddGameForm()
        if add_game.validate_on_submit():
                add_game_to_db = Games(
                                name = add_game.game_name.data,
                                genre_id = add_game.genre_id.data,
                                price = add_game.price.data,
                                company = add_game.company.data,
                                main_platform = add_game.main_platform.data,
                                buyer_id = add_game.buyer_id.data
                                )
                db.session.add(add_game_to_db)
                db.session.commit()
                return redirect(url_for('game'))
        else:
                print(add_game.errors)
                gameData = Games.query.all()
        return render_template('game.html', title='Games', games=gameData, form=add_game)

@app.route('/register', methods=['GET', 'POST'])
def post():
        form = PlayerForm()
        if form.validate_on_submit():
                playerData = players(
                        first_name = form.first_name.data,
                        last_name = form.last_name.data,
                        fav_genre_id = form.fav_genre_id.data,
                        email = form.email.data,
                        fav_game_id = form.fav_game_id.data
                        )
                db.session.add(playerData)
                db.session.commit()
                return redirect(url_for('home'))
        else:
                print(form.errors)

        return render_template('post.html', title='post', form=form)

@app.route('/home/<int:player_id>/update', methods=['GET', 'POST'])
def update():
        form = UpdateForm()
        if form.validate_on_submit():
            current_user.first_name = form.first_name.data
            current_user.last_name = form.last_name.data
            current_user.fav_genre_id = form.fav_genre_id.data
            current_user.email = form.email.data
            current_user.fav_game_id = form.fav_game_id.data
            db.session.commit()
            return redirect(url_for('update'))
        elif request.method == 'GET':
            form.first_name.data = current_user.first_name
            form.last_name.data = current_user.last_name
            form.fav_genre_id.data = current_user.fav_genre_id
            form.email.data = current_user.email
            form.fav_game_id.data = current_user.fav_game_id
        return render_template('update.html', title='Update', form=form)

@app.route('/home/delete', methods=['GET', 'POST'])
def delete():
            delete = DeleteForm()
            customer = Players.query.filter_by(first_name==player_firstname, last_name==player_lastname).first()
            db.session.delete(customer)
            db.session.commit()
            return redirect (url_for('home'))
