class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax()
        self.display_all()
    def tax(self):
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax
        # return self

car1 = Car(2000, "35mph", "100%", "15mpg")

car2 = Car(6000, "5mph", "90%", "20mpg")

car3 = Car(10000, "25mph", "70%", "20mpg")

car4 = Car(25000, "50mph", "40%", "20mpg")

car5 = Car(20000, "59mph", "30%", "20mpg")

car6 = Car(200000, "200mph", "0%", "20mpg")
