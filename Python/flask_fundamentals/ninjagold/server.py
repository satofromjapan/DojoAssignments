from flask import Flask, redirect, request, render_template, session
import random
import datetime
app = Flask(__name__)
app.secret_key = "thesecret"

def makeMoney(start, end):
    money = random.randrange(start,end)
    return money


# def activity(num, location):
#     timestamp = datetime.datetime.now()
#     if location =='farm':
#         session['message'].append('Earned %d from the %s! %s' % (num, location, timestamp))
#     elif location =='house':
#         session['message'].append('Earned %d from the %s! %s' % (num, location, timestamp))
#     elif location =='cave':
#         session['message'].append(['Earned %d from the %s! %s' % (num, location, timestamp)])
#     else:
#         session['message'].append('Earned %d from the %s! %s' % (num, location, timestamp))
new_game=True

@app.route('/')
def index():
    # if session.get('current_gold') == None:
    #     session['current_gold'] = 0
    # if session.get('message') == None:
    #     session['message'] = ["Get Started"]
    global new_game
    if new_game:
        session['current_gold'] = 0
        session['message'] = ["Get Started"]
        new_game=False
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def money():
    timestamp = datetime.datetime.now()
    if request.form['building'] == 'farm':
        session['farmGold'] = makeMoney(10, 20)
        print session['farmGold']
        session['current_gold'] += int(session['farmGold'])
        session['message'].append("Earned " + str(session['farmGold']) + " from the farm! " + str(timestamp))
        # print activity(session['farmGold'], 'farm')
        return redirect('/')
    elif request.form['building'] == 'cave':
        session['caveGold'] = makeMoney(5, 10)
        print session['caveGold']
        session['current_gold'] += int(session['caveGold'])
        session['message'].append("Earned " + str(session['caveGold']) + " from the cave! " + str(timestamp))
        # print activity(session['caveGold'], 'cave')
        return redirect('/')
    elif request.form['building'] == 'house':
        session['houseGold'] = makeMoney(2,5)
        print session['houseGold']
        session['current_gold'] += int(session['houseGold'])
        session['message'].append("Earned " + str(session['houseGold']) + " from the house! " + str(timestamp))
        # print activity(session['houseGold'], 'house')
        return redirect('/')
    else:
        session['casinoGold'] = makeMoney(-50, 50)
        print session['casinoGold']
        session['current_gold'] += int(session['casinoGold'])
        session['message'].append("Earned " + str(session['casinoGold']) + " from the casino! " + str(timestamp))
        # print activity(session['casinoGold'], 'casino')
    print session['message']
    return redirect('/')


app.run(debug = True)
