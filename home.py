from bedroom import Bedroom
from kitchen import Kitchen
from room import Room
from salon import Salon


class Home:
    room_list: list[Room]

    def __init__(self):
        self.room_list = []
        self.radiator_power = 0

    def evaluateRadiatorPower(self):
        self.radiator_power = 0
        for room in self.room_list:
            self.radiator_power = self.radiator_power + room.radiatorPower()

    def addRoom(self, room: Room):
        self.room_list.append(room)
        self.evaluateRadiatorPower()

    def getRadiatorPower(self):
        return self.radiator_power

    def printHome(self):
        pass


if __name__ == '__main__':
    print("Dom")
    salon = Salon(5, 5)
    kitchen = Kitchen(3, 4)

    home = Home()

    home.addRoom(salon)
    home.addRoom(kitchen)
    home.addRoom(Bedroom(3, 3))

    print(home.getRadiatorPower())

    home.printHome()
