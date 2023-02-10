from przyklady.person import Person


class Student(Person):
    def __init__(self, name: str, surname: str, id: int):
        super().__init__(name, surname)
        self.id = id

    def printInfo(self):
        print(f"name: {self.name}, surname: {self.surname}, id: {self.id}")


if __name__ == "__main__":
    student = Student("Przemysław", "Stokłosa", id=10)
    student.printInfo()

