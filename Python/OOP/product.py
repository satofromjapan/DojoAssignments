class product(object):
    def __init__(self, price, item_name, weight, brand, cost, status = "for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = "sold"
        return self
    def addtax(self, tax):
        self.price = self.price + (self.price * tax)
        return self
    def product_return(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.price = self.price * 0.8
        return self
    def displayInfo(self):
        print "Item name:", self.item_name
        print "Price:", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status

product1 = product(2, "Banana", "100g", "Delmonte", 1).addtax(0.12).product_return("opened").displayInfo()

product2 = product(10, "Strawberries", "90g", "Some farm", 4).sell().displayInfo()
