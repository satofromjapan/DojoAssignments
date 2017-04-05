import random


def score():
    for i in range(10):
        random_num = random.randint(60,100)
        if random_num >= 90:
            print "Score: ", random_num, "; Your Grade is A"
        elif random_num >= 80:
            print "Score: ", random_num, "; Your Grade is B"
        elif random_num >= 70:
            print "Score: ", random_num, "; Your Grade is C"
        elif random_num >= 60:
            print "Score: ", random_num, "; Your Grade is D"

score()
