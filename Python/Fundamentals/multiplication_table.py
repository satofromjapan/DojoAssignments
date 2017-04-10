for row in range(1, 13):
    s = ''
    for col in range(1,13):
        s += '{:3}'.format(row*col)
    print s
