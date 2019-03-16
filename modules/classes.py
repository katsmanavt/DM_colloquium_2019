class Natural (list):
    def __init__ (self, n = 0, a1=0, *args):
        self.n = n
        super().__init__(tuple([a1]+list(args)))
    
    
    def copy(self):
        return Natural(self.n, *super().copy())
    

class Integer(Natural):
    def __init__(self, b = 0, n = 0, a1=0, *args):
        self.b = b
        super().__init__(n, tuple([a1]+list(args)))
    
    
    def copy(self):
        return Integer(self.b, self.n, *super().copy())


class Rational:
    def __init__(self, m = Integer(), n = Natural()):
        self.m = m
        self.n = n
    
    
    def copy(self):
        return Rational(self.m.copy(), self.n.copy())
        

class Polinomial (list):
    def __init__ (self, m = 0, a1=0, *args):
        self.m = m
        super().__init__(tuple([a1]+list(args)))
        
    
    def copy(self):
        return Polinomial(self.m, *super().copy())
