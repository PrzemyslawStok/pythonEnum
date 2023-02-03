from Figures2D.square import Square
from Figures2D.triangle import Triangle
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
        area = 0
        for room in self.room_list:
            area = area + room.roomArea()
            room.printInfo()

        print(f"__________________________________________")
        print(f"powierzchnia całkowita: {area}")
        print(f"całkowite zapotrzebowanie energetyczne: {self.getRadiatorPower()}")


if __name__ == '__main__':
    print("Dom")
    #salon = Salon(5, 5)
    #kitchen = Kitchen(3, 4)

    home = Home()

    #home.addRoom(salon)
    #home.addRoom(kitchen)
    home.addRoom(Bedroom(Square(5)))
    home.addRoom(Bedroom(Square(7)))

    home.printHome()
