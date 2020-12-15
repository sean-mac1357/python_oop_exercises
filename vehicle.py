class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print("My car is a :{}, {}, {}.".format(self.year, self.make, self.model))

car = Vehicle('Ram', '1500', '2014')
print(car.print_info())