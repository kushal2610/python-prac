class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display(self):
        return self.brand, self.model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_car = ElectricCar("Kia", "Ev6", "60Kwh")
print(my_car.display())