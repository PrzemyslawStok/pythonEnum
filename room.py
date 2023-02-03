from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, a: float, b: float):
        self.radiator_power_area = 0.2
        self.name = "room"

        self.a = a
        self.b = b

    @abstractmethod
    def roomArea(self) -> float:
        pass

    @abstractmethod
    def radiatorPower(self) -> float:
        pass

    def printInfo(self):
        print(
            f"nazwa: {self.name}, powierzchnia: {self.roomArea()}, zapotrzebowanie energetyczne: {self.radiatorPower()} kWh")
