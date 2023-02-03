from abc import abstractmethod


class Figure2D():
    def __init__(self, name: str = None):
        self.name = name

    @abstractmethod
    def area(self)->float:
        pass

    @abstractmethod
    def perimeter(self)->float:
        pass

    def __str__(self):
        return f"powierzchnia ({self.name}): {self.area()}, obwód: {self.perimeter()}"
