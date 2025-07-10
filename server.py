from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/editor/<name>')
def editor(name):
    return render_template('editor.html', assignment_name=name, directions='write fibonacchi', test_case_list=[{
        'input': '1\n2\n3',
        'output': 'swg\n\n\n\nsawgsawg'
    },{
        'input': '1\n2\n3',
        'output': 'swg\n\n\n\nsawgsawg'
    },{
        'input': '1\n2\n3',
        'output': 'swg\n\n\n\nsawgsawg'
    },])

app.run(debug=True)