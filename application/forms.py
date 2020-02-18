from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length
from application.models import Players, Genres, Games
from application import app


class PlayerForm(FlaskForm):
	first_name = StringField('First Name',
		validators = [
			DataRequired(),
			Length(min=2, max=30)
		]
	)
	last_name = StringField('First Name',
		validators = [
			DataRequired(),
			Length(min=2, max=30)
		]
	)
	fav_genre_id = IntegerField('Genre ID',
		validators = [
			DataRequired(),
			NumberRange(min=1, max=100)
		]
	)
	email = StringField('Email',
		validators = [
			DataRequired(),
			email
		]
	)
	submit = SubmitField('Post!')

class AddGenreForm(FlaskForm):
	genre_name = StringField('Genre Name',
		validators = [
			DataRequired(),
			Length(min=2, max=30)
		]
	)
	submit = SubmitField('Add!')

class AddGameForm(FlaskForm):
	game_name = StringField('Game Name',
		validators = [
			DataRequired(),
			Length(min=2, max=30)
		]
	)
	genre_id = IntegerField('Genre ID',
                validators = [
                        DataRequired(),
                        NumberRange(min=1, max=100)
                ]
        )
	Price = DecimalField('Price', places=2
		validators = [
			DataRequired()
		]
	)
	company = StringField('Comapany',
			validators = [
				DataRequired(),
				Length(min=2, max=30)
		]
	)
	main_platform = StringField('main platform',
			validators = [
				DataRequired()
				Length(min=2, max=30)
