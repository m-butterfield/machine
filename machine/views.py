from machine import app
from flask import render_template

@app.route('/')
@app.route('/examples/<int:example_id>')
def index(example_id=1):
    return render_template('index.html')
