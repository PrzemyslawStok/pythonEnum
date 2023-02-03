from Figures2D.figure2D import Figure2D
import numpy as np


class Triangle(Figure2D):
    def __init__(self, a: float = None):
        super().__init__(name="trójkąt")
        self.a = a

    def area(self):
        return np.sqrt(3) / 4.0 * self.a * self.a
