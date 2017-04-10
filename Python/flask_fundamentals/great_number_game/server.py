from flask import Flask, flash, redirect, request, session, render_template
import random

app = Flask(__name__)
app.secret_key = "secretforgame"

def randomNum():
    session['gameNum'] = random.randrange(0, 101)

@app.route('/')
def index():
    # if session['gameNum'] != None:
    #     pass
    # else:
    #     randomNum()
    # print session['gameNum']
    if session.get('gameNum') == None:
        session['gameNum']= random.randint(0,100)

    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    # print session['gameNum']
    print request.form['guess']
    print session['gameNum']
    error = None
    # if request.method == 'POST':
    if int(request.form['guess']) == int(session['gameNum']):
        print "correct"
        session['message'] = "You guessed it!"
        return redirect('/')
    elif int(request.form['guess']) < int(session['gameNum']):
        print "low"
        session['message'] = "Too low"
        return redirect('/')
        # session.pop('guess')
    else:
        print "high"
        session['message'] = "Too high"
        # session.pop('guess')

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    # session.pop('gameNum')
    session.pop('message')
    session.pop('gameNum')
    return redirect('/')

app.run(debug=True)
