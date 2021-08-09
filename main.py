import flask
from app import app, db
from app.models import User


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Game': Game}


if __name__ == '__main__':
    app.run(debug=True)