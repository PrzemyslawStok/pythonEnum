from przyklady.person import Person

class Teacher(Person):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
