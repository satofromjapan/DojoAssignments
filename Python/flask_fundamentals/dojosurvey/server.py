from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def create_user():
    print "It's working!"
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("result.html", name = name, location = location, language = language, comment = comment)


app.run(debug=True)
