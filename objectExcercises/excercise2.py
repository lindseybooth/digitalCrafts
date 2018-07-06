class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def carInfo(self):
        return "{} {} {}".format(self.make, self.model, self.year)
    
myCar = Vehicle("Ford", "Escape", 2015)

print(Vehicle.carInfo(myCar))