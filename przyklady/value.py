class Value():
    def __init__(self, value: float):
        self.value = value

    def printValue(self):
        print(self.value)


if __name__ == "__main__":
    number0 = Value(10.0)
    number1 = Value(11.0)

    number_list: list[Value] = []

    number_list.append(number0)
    number_list.append(number1)

    for number in number_list:
        number.printValue()
