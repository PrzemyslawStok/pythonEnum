class Figure2D():
    def __init__(self, name: str = None):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass

    def __str__(self):
        return f"powierzchnia ({self.name}): {self.area()}, obwód: {self.perimeter()}"
