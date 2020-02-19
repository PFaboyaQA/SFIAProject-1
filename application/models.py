from application import db

class Players(db.Model):
        player_id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(30), nullable=False)
        last_name = db.Column(db.String(30), nullable=False)
        fav_genres = db.relationship('Genres', backref='playergenre', lazy=True)
        email = db.Column(db.String(50), nullable=False, unique=True)
        games = db.relationship('Games', backref='player', lazy=True)

        def __repr__(self):
                return ''.join([
                        'player: ', self.first_name, ' ', self.last_name, ' ', self.email, '\r\n'
                        ])


class Genres(db.Model):
        genre_id = db.Column(db.Integer, primary_key=True)
        genre_name = db.Column(db.String(30), nullable=False)
        player_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
        game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)

        def __repr__(self):
                'genre: ', self.genre_name, '\r\n'

class Games(db.Model):
        game_id = db.Column(db.Integer, primary_key=True)
        game_name = db.Column(db.String(30), nullable=False)
        Price = db.Column(db.Integer, nullable=False)
        company = db.Column(db.String(40), nullable=False)
        main_platform = db.Column(db.String(30), nullable=False)
        buyer_id = db.Column(db.Integer, db.ForeignKey('players.player_id'), nullable=False)
        genre = db.relationship('Genres', backref='game', lazy=True)

        def __repr__(self):
                'game: ', self.game_name, self.company, self.main_platform, '\r\n'
                'sale: ', self.buyer_id, self.price
