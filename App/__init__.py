from flask import render_template, redirect, Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index_page():
    return render_template('index.html')


@app.route('/about')
def about_page():
    return render_template('about.html')