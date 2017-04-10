class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        #display the bike's price, max speed, and total miles
        print "Price:", self.price, "Max speed:", self.max_speed, "Miles:", self.miles
        return self
    def ride(self):
        #show "riding" on the screen and increase the tital miles ridden by 10
        self.miles = self.miles + 10
        print "Riding", self.miles
        return self
    def reverse(self):
        #show "reversing" on the screen and decrease the total miles ridden by 5
        if self.miles > 0:
            self.miles = self.miles - 5
            print "Reversing", self.miles
        else:
            print "Negative miles not allowed!"
        return self

bike1 = Bike(200, "25mph").ride().ride().ride().reverse().displayInfo()

bike2 = Bike(150, "20mph").ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(100, "15mph").reverse().reverse().reverse().displayInfo()
