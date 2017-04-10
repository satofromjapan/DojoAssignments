from flask import Flask, render_template, redirect, request
app= Flask(__name__)

@app.route('/')
def index():
    return 'No ninjas here'

@app.route('/ninja')
def ninja():
    return render_template('index.html', allNinjas=True)

@app.route('/ninja/<ninja_color>')
def color(ninja_color):
    return render_template('ninja.html', color = ninja_color, allNinjas = False)

app.run(debug=True)
