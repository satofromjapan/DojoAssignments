#l = ['magical unicorns',19,'hello',98.98,'world']
#l = [2,3,1,7,4,12]
l = ['magical','unicorns']

def typeList(l):
    string = ''
    sum = 0
    sCount = 0
    iCount = 0
    for element in l:
        if type(element) == str:
            string = string + element + " "
            sCount = sCount + 1
        if type(element) == int:
            sum = sum + element
            iCount = iCount + 1
        elif type(element) == float:
            sum = sum + element
            iCount = iCount + 1
    if iCount > 0 and sCount > 0:
        print "The array is mixed type"
        print "Sum:", sum
        print "String:", string
    elif iCount > 1 and sCount < 1:
        print "The array is of integer type"
        print "Sum:", sum
    elif iCount < 1 and sCount > 0:
        print "The array is of string type"
        print "String:", string

typeList(l)
