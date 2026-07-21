class Car:
    total = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total+=1
    def display(self):
        return self.__brand, self.__model
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        return "Petrol/Diesel"
    @staticmethod
    def car_description():
        return f"It's a Car"
    @property
    def model(self):
        return self.__model


    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "charge"


my_car = ElectricCar("Kia", "Ev6", "60Kwh")
# print(Car.model())

my_car2 = Car("Honda", "City")
print(my_car2.model)
# print(Car.total)
# print(my_car.get_brand())
# print(my_car.__brand)
# print(my_car.fuel_type)