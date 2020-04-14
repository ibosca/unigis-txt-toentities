class Teacher(Person):

    def __init__(self, isExternal: bool):
        self.isExternal = isExternal
    
    def isExternal(self) -> bool:
        return self.isExternal
