def foobar():
    for i in range(100,100001):
        def sqrt(i):
            rt = 0
            while rt * rt < i:
                rt = rt + 1
            if rt * rt != i:
                return False
            else:
                return True
        if sqrt(i) is True:
            # print i
            print "Bar"
        elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            # print i
            print "Foo"
        else:
            # print i
            print "FooBar"

foobar()
