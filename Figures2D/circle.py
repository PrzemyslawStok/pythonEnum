from Figures2D.figure2D import Figure2D
import numpy as np


class Circle(Figure2D):
    def __init__(self, r: float = None):
        super().__init__(name="koło")
        self.r = r

    def area(self):
        return np.pi * self.r * self.r
