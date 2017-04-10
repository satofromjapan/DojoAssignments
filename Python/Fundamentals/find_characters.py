l = ['hello','world','my','name','is','Anna']
char = 'o'

def findChar(l, char):
    new = []
    for element in l:
        if char in element:
            new.append(element)
    print new

findChar(l, char)
