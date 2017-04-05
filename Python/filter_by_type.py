#Integer
'''
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23


def integer(int):
#Find type
    print type(int)
    if int >= 100:
        print "That's a big number!"
    elif int < 100:
        print "That's a small number"

integer(sI)
integer(mI)
integer(bI)
integer(eI)
integer(spI)
#String

sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""

def string(str):
    print type(str)
    if len(str) >= 50:
        print "Long sentence."
    else:
        print "Short sentence."

string(sS)
string(mS)
string(bS)
string(eS)
'''
#List

aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

def list(lst):
    print type(lst)
    if len(lst) >= 10:
        print "Big list!"
    else:
        print "Short list."

list(aL)
list(mL)
list(lL)
list(eL)
list(spL)
