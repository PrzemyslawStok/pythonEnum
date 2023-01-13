from enum import Enum, unique, auto

@unique
class Colors(Enum):
    RED = 10
    GREEN = 11
    BLUE = 12

def f0() -> tuple[Colors.RED, Colors.BLUE]:
    return Colors.RED, Colors.GREEN


if __name__ == '__main__':
    print("pyton 3.11")
    print(Colors.RED)

    print(type(Colors.RED))

    print(f0())

    colorList = [Colors.RED, Colors.BLUE]
    color0 = Colors.GREEN

    if color0 in colorList:
        print("Kolor znajduje się na liście")
    else:
        print("Nieprawidłowy kolor")

    print(f"{Colors.RED.name}: {Colors.RED.value}")
    print(Colors(Colors.RED))

    print(Colors(10))
