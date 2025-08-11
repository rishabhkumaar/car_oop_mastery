from core.vehicle import Car, ElectricCar, SportsCar
from core.engine import Engine
from utils.persistence import save_garage, load_garage

def main():
    garage = load_garage()

    if not garage:
        garage = [
            Car("Toyota", "Camry", 2022, Engine("Petrol")),
            ElectricCar("Tesla", "Model S", 2024, 100),
            SportsCar("Ferrari", "488", 2021)
        ]

    print("=== Car CLI ===")
    while True:
        print("\n1. View Cars\n2. Start Engines\n3. Save & Exit")
        ch = input("Enter: ")

        if ch == "1":
            for c in garage:
                print("→", c.car_info())
        elif ch == "2":
            for c in garage:
                print(f"{c.get_brand()} ➤ {c.start_engine()}")
        elif ch == "3":
            save_garage(garage)
            print("✅ Garage saved. Exiting.")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()

'''
from abc import ABC, abstractmethod
from datetime import datetime

# 1. Interface (Abstract Base Class)
class Vehicle(ABC):
    @abstractmethod
    def car_info(self):
        pass

    @abstractmethod
    def start_engine(self):
        pass


# 2. Composition - Engine class
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        return f"{self.engine_type} engine started."


# 3. Base Car class (implements Vehicle)
class Car(Vehicle):
    wheels = 4  # Class variable

    def __init__(self, brand, model, year, engine: Engine):
        self.__brand = brand            # Encapsulation
        self.__model = model
        self.__year = year
        self.engine = engine            # Composition

    def car_info(self):
        return f"{self.__year} {self.__brand} {self.__model}"

    def start_engine(self):
        return self.engine.start()

    @classmethod
    def general_info(cls):
        return f"Cars typically have {cls.wheels} wheels."

    @staticmethod
    def vehicle_type():
        return "This is a motor vehicle."

    # Encapsulation via getters and setters
    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand


# 4. Inheritance: ElectricCar subclass
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year, Engine("Electric"))
        self.battery_capacity = battery_capacity

    def car_info(self):
        base = super().car_info()
        return f"{base} with {self.battery_capacity} kWh battery"


# 5. Polymorphism: SportsCar subclass
class SportsCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year, Engine("Turbo Petrol"))

    def car_info(self):
        return f"{super().car_info()} [⚡ Sports Mode Enabled]"


# 6. File Logger for Logging Actions
class Logger:
    @staticmethod
    def log(message):
        with open("logs.txt", "a") as file:
            file.write(f"[{datetime.now()}] {message}\n")


# ========== CLI Interaction ==========

def main():
    Logger.log("=== Program Started ===")

    # Object creation
    car1 = Car("Toyota", "Camry", 2022, Engine("Petrol"))
    car2 = ElectricCar("Tesla", "Model S", 2024, 100)
    car3 = SportsCar("Lamborghini", "Huracan", 2023)

    garage = [car1, car2, car3]

    print("🚗 Welcome to Car OOP Mastery 🚗")
    print("--------------------------------")

    while True:
        print("\nChoose an option:")
        print("1. Show all cars")
        print("2. Start all engines")
        print("3. Change brand of a car")
        print("4. View general car info")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\n📋 Car Details:")
            for car in garage:
                print("→", car.car_info())
                Logger.log(f"Viewed: {car.car_info()}")

        elif choice == "2":
            print("\n🔧 Starting Engines:")
            for car in garage:
                print(f"{car.get_brand()} -> {car.start_engine()}")
                Logger.log(f"Started engine of: {car.car_info()}")

        elif choice == "3":
            print("\n✏️ Change Brand")
            for idx, car in enumerate(garage):
                print(f"{idx + 1}. {car.get_brand()}")
            try:
                index = int(input("Choose car number: ")) - 1
                new_brand = input("Enter new brand name: ")
                garage[index].set_brand(new_brand)
                Logger.log(f"Changed brand of car {index + 1} to {new_brand}")
                print("✅ Brand updated.")
            except:
                print("❌ Invalid input.")

        elif choice == "4":
            print("\nℹ️ General Info:")
            print(Car.general_info())
            print(Car.vehicle_type())

        elif choice == "5":
            print("👋 Exiting program. Check logs.txt for logs.")
            Logger.log("Program exited.")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
'''