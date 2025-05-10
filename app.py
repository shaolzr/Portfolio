from flask import Flask, render_template
from flask import send_from_directory
import os

app = Flask(__name__, static_folder='static', template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/task_tracker')
def task_tracker():
    return render_template('task_tracker.html')

if __name__ == '__main__':
    app.run(debug=True) 