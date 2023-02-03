from abc import ABC, abstractmethod
from Figures2D.figure2D import Figure2D

class Room(ABC):
    def __init__(self, base: Figure2D):
        self.radiator_power_area = 0.2
        self.name = "room"

        self.base = base

    @abstractmethod
    def roomArea(self) -> float:
        pass

    @abstractmethod
    def radiatorPower(self) -> float:
        pass

    def printInfo(self):
        print(
            f"nazwa: {self.name}, powierzchnia: {self.roomArea()}, zapotrzebowanie energetyczne: {self.radiatorPower()} kWh")
