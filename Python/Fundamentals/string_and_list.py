#Find and Replace
'''
str = "It's thanksgiving day. It's my birthday,too!"
print str.find ('day')
print str.replace('day', 'month')


#Min and Max
x = [2,54,-2,7,12,98]
max = max(x)
min = min(x)

print "Max is :", max, "Min is:", min

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
first = x[0]
last = x[len(x) - 1]
firstlast = []

firstlast.append(first)
firstlast.append(last)

print firstlast
'''

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort();
first = x[:len(x)/2]
last = x[len(x)/2:]
last.insert(0, first)
print last
