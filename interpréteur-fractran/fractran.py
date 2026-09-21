class Fraction : 
    def __init__(self,numérateur,dénominateur):
        self.numérateur = numérateur
        self.dénominateur = dénominateur

    def est_entier(self,n):
        if n % self.dénominateur == 0:
            return True
        return False

    def valeur(self,n):
        return self.numérateur*(n//self.dénominateur)


class Facteur :
    def __init__(self,facteurs):
        self.facteurs = facteurs

    def nombre(self,exposants):
        nombre = 1
        for i in range(len(exposants)):
            nombre = nombre * (self.facteurs[i]**exposants[i])
        return nombre

    def décomposition(self,n):
        exposants = []
        for facteur in self.facteurs:
            exposant = 0
            while n % facteur == 0:
                exposant += 1
                n = n // facteur
            exposants.append(exposant)
        return exposants


class Fractran:
    def __init__(self, fractions):
        self.programme = fractions

    def run(self, n):
        i = 0
        while i < len(self.programme):
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                i = 0
            else:
                i += 1
        return n

    def suite(self, n, N):
        L=[n]
        i=0
        while i < len(self.programme) and len(L) < N:
            if self.programme[i].est_entier(n):                    
                n = self.programme[i].valeur(n)
                L.append(n)
                i = 0
            else:
                i += 1
        return L
