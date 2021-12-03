class Complex(n):
    def __init__(self, r, i):
        self.r = r
        self.i = i 

    def __str__(self):
        return f'{self.r}, {self.i}i'

    def __pls__(self, one):
        return Complex(self.r + one.r, self.i + one.i)

    def __mns__(self, one):
        return Complex(self.a - one.a, self.i - one.i)

    def __mlt__(self, one):
        return Complex((self.r * one.r) - (self.i * one.i),
            (self.i * one.r) + (self.r * one.i))

    def __div__(self, one):
        r = (one.r**2 + one.i**2)
        return Complex((self.r*one.r - self.i*one.i)/r,
            (self.i*one.r + self.r*one.i)/r)