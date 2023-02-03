from Figures2D.circle import Circle
from Figures2D.figure2D import Figure2D
from Figures2D.square import Square
from Figures2D.triangle import Triangle


def addArea(figures_list: list[Figure2D]) -> float:
    areaSum = 0
    for figure in figures_list:
        areaSum += figure.area()

    return areaSum


if __name__ == "__main__":
    square = Square(a=10)
    circle = Circle(r=5)

    figures_list: list[Figure2D] = []

    figures_list.append(square)
    figures_list.append(circle)
    figures_list.append(Square(1))
    # figures_list.append(10)

    figures_list.append(Triangle(5))
    figures_list.append(Triangle(10))

    for figure in figures_list:
        print(figure)

    print(f"Sumaryczne pole powierzchni wynosi: {addArea(figures_list)}")
