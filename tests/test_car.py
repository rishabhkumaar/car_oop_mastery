import unittest
from core.vehicle import Car, ElectricCar, SportsCar
from core.engine import Engine

class TestCars(unittest.TestCase):
    def test_car_info(self):
        car = Car("Toyota", "Yaris", 2020, Engine("Petrol"))
        self.assertIn("Toyota", car.car_info())

    def test_electric_car(self):
        tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
        self.assertIn("75", tesla.car_info())

    def test_sports_car(self):
        lambo = SportsCar("Lambo", "Huracan", 2022)
        self.assertIn("Sports Mode", lambo.car_info())

if __name__ == "__main__":
    unittest.main()
