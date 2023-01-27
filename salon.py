from room import Room


class Salon(Room):
    def __init__(self, a: float, b: float):
        super().__init__(a, b)
        self.radiator_power_area = 0.1
        self.name = "Salon"

    def roomArea(self):
        return self.a * self.b

    def radiatorPower(self):
        return self.roomArea() * self.radiator_power_area
