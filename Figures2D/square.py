from Figures2D.figure2D import Figure2D


class Square(Figure2D):
    def __init__(self, a: float):
        super().__init__(name="kwadrat")
        self.a = a

    def area(self):
        return self.a * self.a
