from flask import render_template, url_for, redirect, request
from application import app, db
from application.forms import AddGenreForm, AddGameForm, PlayerForm, DeleteForm, UpdateForm, DeleteGenreForm, DeleteGameForm, AddPlayerGame
from application.models import Players, Genres, Games

@app.route('/')
@app.route('/home')
def home():
        playerData = Players.query.all()
       # fav=Genres.query.filter_by(genre_id==Players.fav_genre).first()
        return render_template('home.html', title='Home', players=playerData)

@app.route('/genre', methods=['GET', 'POST'])
def genre():
        add_genre = AddGenreForm()
        if add_genre.validate_on_submit():
                add_genre_to_db = Genres(
				genre_name = add_genre.genre_name.data,
				)
                db.session.add(add_genre_to_db)
                db.session.commit()
                return redirect(url_for('genre'))
        else:
	        print(add_genre.errors)
	        genreData = Genres.query.all()
        return render_template('genre.html', title='Genre', genres=genreData, form=add_genre)

@app.route('/game/<player_id>')
def player_game(player_id):
    player = Players.query.filter_by(player_id = player_id).first()
    form = AddPlayerGame()
    if form.validate_on_submit():
        form_to_db = Games(
                game_name=form.game_name.data,
                playergame = player)
        return redirect (url_for('home'))
    elif request.method == "GET":
        form.game_name.data = Games.game_name
    return render_template('player_game.html', title='players games', form=form)

@app.route('/game', methods=['GET', 'POST'])
def game():
        add_game = AddGameForm()
        if add_game.validate_on_submit():
                add_game_to_db = Games(
                                game_name = add_game.game_name.data,
                                Price = add_game.price.data,
                                company = add_game.company.data,
                                main_platform = add_game.main_platform.data,
                                buyer_id = add_game.buyer_id.data,
                                genre_id = add_game.genre_id.data
                                )
                db.session.add(add_game_to_db)
                db.session.commit()
                return redirect(url_for('game'))
        else:
                print(add_game.errors)
                gameData = Games.query.all()
        return render_template('game.html', title='Game', games=gameData, form=add_game)

@app.route('/register', methods=['GET', 'POST'])
def post():
        form = PlayerForm()
        if form.validate_on_submit():
                playerData = Players(
                        first_name = form.first_name.data,
                        last_name = form.last_name.data,
                        email = form.email.data
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
            current_user.email = form.email.data
            current_user.fav_game_id = form.fav_game_id.data
            db.session.commit()
            return redirect(url_for('update'))
        elif request.method == 'GET':
            form.first_name.data = current_user.first_name
            form.last_name.data = current_user.last_name
            form.email.data = current_user.email
            form.fav_game_id.data = current_user.fav_game_id
        return render_template('update.html', title='Update', form=form)

@app.route('/delete', methods=['GET', 'POST'])
def delete(): 
            delete = DeleteForm()
            if delete.validate_on_submit():
                customer = Players.query.filter_by(first_name=delete.player_firstname.data, last_name=delete.player_lastname.data).first()
                #games = Games.query.filter_by(buyer_id=customer.player_id)
                #for game in games:
                 #   db.session.delete(game)
                db.session.delete(customer)
                db.session.commit()
                return redirect (url_for('home'))
            else:
                print("doesnt work")
            delete_genre = DeleteGenreForm()
            if delete_genre.validate_on_submit():
                category = Genres.query.filter_by(genre_name=genrename).first()
                db.session.delete(category)
                db.session.commit()
                return redirect (url_for('genre'))
            delete_game = DeleteGameForm()
            if delete_game.validate_on_submit():
                item = Games.query.filter_by(game_name=gamename).first()
                db.session.delete(item)
                db.session.commit()
                return redirect (url_for('game'))
            return render_template('delete.html', title='Delete', delete=delete, delete_genre=delete_genre, delete_game=delete_game)
            
@app.route('/home/<player_id>', methods=['GET','POST'])
def playerid(player_id):
    playerData = Players.query.filter_by(player_id=player_id).first()
    print(playerData)
    form = UpdateForm()
    if form.validate_on_submit():
        playerData.first_name=form.first_name.data
        playerData.last_name=form.last_name.data
        playerData.email=form.email.data
        db.session.add(playerData)
        db.session.commit()
        return redirect (url_for('home'))
    return render_template('playerid.html', title='Player', player=playerData, form=form)


