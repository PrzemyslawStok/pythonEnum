from abc import ABC, abstractmethod

class Room(ABC):
    @abstractmethod
    def roomArea(self):
        pass
    @abstractmethod
    def radiatorPower(self):
        pass