from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, a: float, b: float):
        self.radiator_power_area = 0.2

        self.a = a
        self.b = b

    @abstractmethod
    def roomArea(self) -> float:
        pass

    @abstractmethod
    def radiatorPower(self) -> float:
        pass
