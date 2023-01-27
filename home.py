from kitchen import Kitchen
from room import Room
from salon import Salon


class Home:
    room_list: list[Room]
    radiator_power = 0

    def __init__(self):
        self.room_list = []

    def evaluateRadiatorPower(self):
        self.radiator_power = 0
        for room in self.room_list:
            self.radiator_power = self.radiator_power + room.radiatorPower()

    def addRoom(self, room: Room):
        self.room_list.append(room)
        self.evaluateRadiatorPower()

    @classmethod
    def getRadiatorPower(self):
        return self.radiator_power


if __name__ == '__main__':
    print("Dom")
    salon = Salon(5, 5)
    kitchen = Kitchen()

    home = Home()
    home.addRoom(salon)
    print(home.getRadiatorPower())
