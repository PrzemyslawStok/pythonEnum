from room import Room

class Bedroom(Room):
    def __init__(self, a: float, b: float):
        super().__init__(a, b)
        self.name = "Łazienka"
        self.radiator_power_area = 0.5

    def roomArea(self):
        return self.a * self.b

    def radiatorPower(self):
        return self.radiator_power_area * self.roomArea()

