class figure2d:
    a = 100
    b = 100

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def printInfo():
        print(f"info: figure2d")

    def printArea(self):
        print(f"area: {self.a * self.b}")

    @classmethod
    def printArea_1(cls):
        print(f"area: {cls.a * cls.b}")


if __name__ == "__main__":
    figure = figure2d(5, 5)
    figure1 = figure2d(10, 10)

    figure.printArea()
    figure1.printArea()

    figure.printArea_1()

    figure2d.printInfo()
