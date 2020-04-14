class Student(Person):

    def __init__(self, hasInstallmentPayment: bool):
        self.hasInstallmentPayment = hasInstallmentPayment

    def hasInstallmentPayment(self) -> bool:
        return self.hasInstallmentPayment

