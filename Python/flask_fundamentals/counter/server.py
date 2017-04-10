from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'secretkey'

def accessCounter():
    try:
        session['count'] += 1
    except KeyError:
        session['count'] = 1

@app.route('/')
def index():
    accessCounter()
    # session['count'] += 1
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    accessCounter()
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
