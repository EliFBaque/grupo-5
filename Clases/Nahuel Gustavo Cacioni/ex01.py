#1 - Crear una clase que represente un numero complejo. Tenga 4 metodos que permita las operaciones matematicas basicas (+,-,*,/).

class complex:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def sum(self):
        return self.n1 + self.n2

    def substraction(self,n1,n2):
        return self.n1 - self-n2

    def multiplication(self,n1,n2):
        return self.n1 * self.n2

    def division(self,n1,n2):
        return self.n1 / self.n2