from core.vehicle import Car
from core.engine import Engine

class Bike(Car):
    wheels = 2

    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year, Engine("Petrol"))
        self.engine_cc = engine_cc

    def car_info(self):
        return f"{super().car_info()} [{self.engine_cc}cc Bike]"

    def get_wheels(self):
        return self.wheels
