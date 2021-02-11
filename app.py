from XLSXParser import Parser
from flask import Flask, render_template,url_for

app = Flask(__name__)


@app.route('/')
def welcome_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
