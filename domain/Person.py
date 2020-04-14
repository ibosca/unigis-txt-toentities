class Person():

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def getName(self) -> str:
        return self.name

    def getSurname(self) -> str:
        return self.surname

