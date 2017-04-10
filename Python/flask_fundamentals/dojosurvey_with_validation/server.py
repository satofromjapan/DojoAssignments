from flask import Flask, render_template, redirect, request, flash
app = Flask(__name__)
app.secret_key = 'Thisissecret'

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
    if len(request.form['name']) < 1:
        flash("Name cannot be blank!")
        return redirect('/')
    elif len(request.form['comment']) < 1:
        flash("Fill in the comment field")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Make your comment less than 120 characters.")
        return redirect('/')
    else:
        flash("Success!")
    return render_template("result.html", name = name, location = location, language = language, comment = comment)


app.run(debug=True)
