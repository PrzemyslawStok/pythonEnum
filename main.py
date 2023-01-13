from enum import Enum, unique, auto


@unique
class Colors(Enum):
    RED = 10,
    GREEN = 2,
    BLUE = 10


def f0(a: tuple[str, int]) -> tuple[str, int]:
    return "a", 1


if __name__ == '__main__':
    print("pyton 3.11")
    print(Colors.RED)

    print(type(Colors.RED))

    f0(a=("a", 1))

    colorList = [Colors.RED, Colors.BLUE]
    color0 = Colors.GREEN

    if color0 in colorList:
        print("Kolor znajduje się na liście")
    else:
        print("Nieprawidłowy kolor")

    print(f"{Colors.RED.name}: {Colors.RED.value}")
