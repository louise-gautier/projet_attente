from flask import render_template
from app import app


@app.route('/')
@app.route('/ligues/')
@app.route('/profil/')
@app.route('/login/')
def attente():
    return render_template('attente.html')

