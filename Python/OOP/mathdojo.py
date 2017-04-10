class mathdojo(object):
    def __init__(self):
        self.final = 0
    def add(self, *param):
        for i in range(0,len(param)):
            if isinstance(param[i], list):
                self.final += sum(param[i])
            else:
                self.final += param[i]
        return self
    def subtract(self, *param):
        for i in range(0,len(param)):
            if isinstance(param[i], list):
                self.final -= sum(param[i])
            else:
                self.final -= param[i]
        return self
    def result(self):
        print self.final

# md = mathdojo().add(2).add(2, 5).subtract(3, 2).result()
md = mathdojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
