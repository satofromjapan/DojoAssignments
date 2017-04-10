class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "Name:", self.name
        print "Health:", self.health
        return self

# animal1 = Animal("Panda").walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

# dog = Dog("Spot").walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "this is a dragon"
        return super(Dragon, self).displayHealth()

dragon = Dragon("Marvin").displayHealth()

# class Koi(Animal):
#     def __init__(self, name):
#         super(Koi, self).__init__(name)
#         self.health = 90
#
#     def swim(self):
#         self.health -= 5
#         return self
#
# koi = Koi("Fish").walk().swim().displayHealth()
