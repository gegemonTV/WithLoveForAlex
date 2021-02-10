from XLSXParser import Parser
from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome_page():
    return "Welcome!"
