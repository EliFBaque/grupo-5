class Matriz:

    def __init__(self,n1,n2,n3,x):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.x = x

    def pls(self):
        return self.n1 + self.n2

    def mns(self):
        return self.n1 - self.n2

    def mlt(self):
        return self.n3 * self.x