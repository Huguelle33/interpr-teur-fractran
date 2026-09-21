from fractran import Fraction, Facteur, Fractran

somme = [Fraction(3, 2)]
multiplication = [Fraction(455, 33), Fraction(11, 13), Fraction(1, 11), Fraction(3, 7), Fraction(11, 2), Fraction(1, 3)]
facteurs = Facteur([2, 3, 5])

res_add=[]
res_multi=[]
for i in range(1,11):
    for j in range(1,11):
        res_add.append(Fractran(somme).run(facteurs.nombre([i, j])))
        res_multi.append(Fractran(multiplication).run(facteurs.nombre([i, j])))

print("les résultats de l'addition sont :", res_add)
print("les résultats de la multiplication sont :", res_multi)

# explication du code pour la suite de Fibonacci : 

print("Fibonacci rend les couples (F(n), F(n+1)) :")
fibonacci = [Fraction(23, 95), Fraction(57, 23), Fraction(17, 39), Fraction(130, 17), Fraction(11, 14), 
          Fraction(35, 11), Fraction(19, 13), Fraction(1, 19), Fraction(35, 2), Fraction(13, 7), 
          Fraction(7, 1)]

# On commence par 3 car c'est (2**0)*(3**1) et donc les exposants sont (0,1), 
# premiers termes de la suite de Fibonacci. Le programme effectue 1000 étapes.
sortie_brute = Fractran(fibonacci).suite(3, 1000) 

sortie = []
for n in sortie_brute:
    #On vérifie que le nombre est bien de la forme (2**a)*(3**b) pour a et b entiers.
    if n == Facteur([2, 3]).nombre(Facteur([2, 3]).décomposition(n)):
        #Les exposants sont les termes de la suite de Fibonacci.
        sortie.append(Facteur([2, 3]).décomposition(n))
        
print(sortie)




premiers = [Fraction(17, 91), Fraction(78, 85), Fraction(19, 51), Fraction(23, 38), Fraction(29, 33), 
          Fraction(77, 29), Fraction(95, 23), Fraction(77, 19), Fraction(1, 17), Fraction(11, 13), 
          Fraction(13, 11), Fraction(15, 14), Fraction(15, 2), Fraction(55, 1)]

sortie_brute_premiers = Fractran(premiers).suite(2, 100000)

nombres_premiers = []
for i in sortie_brute_premiers:
    if i == Facteur([2]).nombre(Facteur([2]).décomposition(i)):
        exposant = Facteur([2]).décomposition(i)[0]
        if exposant not in nombres_premiers:
            nombres_premiers.append(exposant)

print("Les nombres premiers générés sont :", nombres_premiers)