from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/editor')
def editor():
    return render_template('editor.html')

app.run()