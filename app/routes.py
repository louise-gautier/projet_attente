from flask import render_template
from app import app


@app.route('/')
@app.route('/ligues/')
@app.route('/profil/')
@app.route('/login/')
def attente():
    return render_template('attente.html')


@app.route('/gif1/')
def gif1():
    return render_template('gif1.html')


@app.route('/gif2/')
def gif2():
    return render_template('gif2.html')

