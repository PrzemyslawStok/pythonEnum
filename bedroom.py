from Figures2D.figure2D import Figure2D
from room import Room


class Bedroom(Room):
    def __init__(self, base: Figure2D):
        super().__init__(base)
        self.name = "Łazienka"
        self.radiator_power_area = 0.5

    def roomArea(self):
        self.base.area()
        return self.a * self.b

    def radiatorPower(self):
        return self.radiator_power_area * self.roomArea()
