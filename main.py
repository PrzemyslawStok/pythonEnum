from enum import Enum, unique, auto


@unique
class Colors(Enum):
    RED = 10
    GREEN = 11
    BLUE = 12

    @classmethod
    def f0(cls):
        return Colors.BLUE

    @staticmethod
    def s0():
        return Colors.RED

    @property
    def s1(self):
        return self.RED


def f0() -> list[Colors.RED]:
    return ["sdfsd"]


if __name__ == '__main__':
    print("pyton 3.11")
    print(Colors.RED)

    print(type(Colors.RED))

    print(f0())

    colorList = [Colors.RED, Colors.BLUE]
    color0 = Colors.GREEN

    color1 = Colors.GREEN
    

    if color0 in colorList:
        print("Kolor znajduje się na liście")
    else:
        print("Nieprawidłowy kolor")

    print(f"{Colors.RED.name}: {Colors.RED.value}")
    print(Colors(Colors.RED))



    print(Colors(10))

    color1 = Colors.RED
