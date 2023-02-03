class figure2d:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def printInfo():
        print("figure2d")

    def printArea(self):
        print(f"area: {self.a * self.b}")

    @classmethod
    def printArea_1(cls):
        print("area: ")


if __name__ == "__main__":
    figure = figure2d(5, 5)
    figure1 = figure2d(10, 10)

    figure.printArea()
    figure1.printArea()
