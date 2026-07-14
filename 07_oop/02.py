class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display(self):
        return self.brand, self.model

my_car = Car("Toyota", "Camry")
print(my_car.display())