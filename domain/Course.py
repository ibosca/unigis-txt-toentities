class Course():

    def __init__(self, code: str, name: str, modules: List[Module]):
        self.code = code
        self.name = name
        self.modules = modules

    def getCOde(self) -> str:
        return self.code

    def getName(self) -> str:
        return self.name

    def getModules(self) -> List[Module]:
        return self.modules
