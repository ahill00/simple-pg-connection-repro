from db import session
from flask import Flask


app = Flask(__name__)


@app.route('/')
def foo():
    session.execute('SELECT 1')
    return "ok"


@app.teardown_request
def request_teardown(exception=None):
    session.remove()


@app.teardown_appcontext
def app_teardown(exception=None):
    session.remove()
