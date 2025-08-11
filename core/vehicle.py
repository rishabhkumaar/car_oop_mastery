from core.interfaces import Vehicle
from core.engine import Engine

class Car(Vehicle):
    wheels = 4

    def __init__(self, brand, model, year, engine: Engine):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.engine = engine

    def car_info(self):
        return f"{self.__year} {self.__brand} {self.__model}"

    def start_engine(self):
        return self.engine.start()

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    @classmethod
    def general_info(cls):
        return f"Cars usually have {cls.wheels} wheels."

    @staticmethod
    def vehicle_type():
        return "Motor Vehicle"

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year, Engine("Electric"))
        self.battery_capacity = battery_capacity

    def car_info(self):
        return f"{super().car_info()} with {self.battery_capacity} kWh battery"

class SportsCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year, Engine("Turbo"))

    def car_info(self):
        return f"{super().car_info()} [Sports Mode]"
