from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def car_info(self):
        pass

    @abstractmethod
    def start_engine(self):
        pass
