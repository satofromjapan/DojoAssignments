#Odd/Even

# def odd_even(start, end):
#     for num in range(start, end+1):
#         if num % 2 == 0:
#             print "Number is", num, ". This is an even number."
#
#         else:
#             print "Number is", num, ". This is an odd number."
#
# odd_even(1, 2000)


#Multiply

def multiply(a, mult):
    for num in range(len(a)):
        a[num] *= mult
    return a

# a = [2,4,10,16]
# b = multiply(a,5)
# print b

#HackerChallenge

def hackerChallenge(arr):
    new_arr = []

    for num in arr:
        # print num
        inner_arr =[]
        while num > 0:
            inner_arr.append(1)
            num = num - 1

        new_arr.append(inner_arr)
    return new_arr

x = hackerChallenge(multiply([2,4,5],3))
print x
