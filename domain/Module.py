class Module():

    def __init__(self, code: str, name: str, year: str, isTrunk: bool, teacher: Teacher, students: List[Student]):
        self.code = code
        self.name = name
        self.year = year
        self.isTrunk = isTrunk
        self.teacher = teacher
        self.students = students


    def getCode(self) -> str:
        return self.code

    def getName(self) -> str:
        return self.name

    def getYear(self) -> str:
        return self.year

    def isTrunk(self) -> bool:
        return self.isTrunk

    def getTeacher(self) -> Teacher:
        return self.teacher

    def getStudents(self) -> List[Student]:
        return self.students


