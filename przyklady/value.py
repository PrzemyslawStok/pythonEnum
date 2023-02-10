class Value():
    a = 10

    def __init__(self, value: float):
        self.value = value

    def printValue(self):
        print(self.value)

    @staticmethod
    def info():
        print(f"Value")

    @staticmethod
    def printValues():
        Value.info()
        print(Value.a)

    @classmethod
    def printValue_1(cls):
        print(cls.a)


if __name__ == "__main__":
    number0 = Value(10.0)
    number1 = Value(11.0)

    number_list: list[Value] = []

    number_list.append(number0)
    number_list.append(number1)

    Value.a = 20

    for number in number_list:
        number.printValue()
        #Value.info()
        #Value.printValues()
        number.printValue_1()

