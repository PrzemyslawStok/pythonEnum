from abc import ABC, abstractmethod


class Room(ABC):
    @abstractmethod
    def roomArea(self) -> float:
        pass

    @abstractmethod
    def radiatorPower(self) -> float:
        pass
