from flask import render_template
from app import app


@app.route('/')
def attente():
    return render_template('attente.html')

