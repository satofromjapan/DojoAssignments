import random

def coinToss():

    # print toss
    headCount = 0
    tailCount = 0

    for i in range(5000):
        toss = round(random.random())
        print toss
        if toss == 0.0:
            headCount = headCount + 1
            print "Attempt #", i, "Throwing a coin... It's a head! ... Got", headCount, "head(s) so far and", tailCount, "tail(s) so far"
        else:
            tailCount = tailCount + 1
            print "Attempt #", i, "Throwing a coin... It's a tail! ... Got", headCount, "head(s) so far and", tailCount, "tail(s) so far"

coinToss()
