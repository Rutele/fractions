from math import gcd

class Fraction(object):
    
    nom = None
    denom = None
    
    def __init__(self, nom, denom):
        self.nom = nom 
        self.denom = denom
        
        if self.denom == 0:
            raise ValueError("Denominator must not be zero.")
        
        divisor = gcd(self.nom, self.denom)
        self.nom = int(nom/divisor)
        self.denom = int(denom/divisor)
        
        if (self.denom < 0):
            self.denom = -1 * self.denom
            self.nom = -1 * self.nom

    def __str__(self):
        if self.denom == 1:
            return "{0.nom}".format(self)
        else:
            return "{0.nom}/{0.denom}".format(self)
    
    def __mul__(self, number):
        return Fraction(self.nom*number.nom, self.denom*number.denom)
    
    def __truediv__(self, number):
        return Fraction(self.nom*number.denom, self.denom*number.nom)
    
    def __add__(self, number):
        n1 = self.nom * number.denom 
        n2 = self.denom * number.nom 
        return Fraction(n1+n2, self.denom*number.denom)
    
    def __sub__(self, number):
        n1 = self.nom * number.denom 
        n2 = self.denom * number.nom 
        return Fraction(n1-n2, self.denom*number.denom)

    def __eq__(self, number):
        return self.nom == number.nom and self.denom == number.denom

    def value(self):
        return self.nom/self.denom