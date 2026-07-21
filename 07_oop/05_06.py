class Car:
    total = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total+=1
    def display(self):
        return self.__brand, self.model
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        return "Petrol/Diesel"
    

    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "charge"


my_car = ElectricCar("Kia", "Ev6", "60Kwh")
print(my_car.fuel_type())
my_car2 = Car("Honda", "City")
print(my_car2.fuel_type())
print(Car.total)
# print(my_car.get_brand())
# print(my_car.__brand)
# print(my_car.fuel_type)