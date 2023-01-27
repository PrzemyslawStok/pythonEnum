from room import Room


class Kitchen(Room):

    def __init__(self, a: float, b: float):
        super().__init__(a, b)

    def roomArea(self):
        return self.a * self.b

    def radiatorPower(self):
        return self.radiator_power_area * self.roomArea()
