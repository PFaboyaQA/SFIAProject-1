from flask import render_template
from application import app

@app.route('/')
@app.route('/home')
def home():
	playerData = Players.query.all()
	return render_template('home.html', title='Home', player=playerData)
