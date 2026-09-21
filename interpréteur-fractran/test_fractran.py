from fractran import Fraction, Facteur, Fractran

def test_Fraction_init():
    assert Fraction(1, 2).numérateur == 1
    assert Fraction(1, 2).dénominateur == 2


def test_Fraction_est_entier():
    assert Fraction(1, 2).est_entier(2)
    assert not Fraction(1, 3).est_entier(2)


def test_Fraction_valeur():
    assert Fraction(3, 2).valeur(4) == 3 * (4 // 2)



def test_Facteur_init():
    assert Facteur([2, 3, 7]).facteurs == [2, 3, 7]


def test_Facteur_nombre():
    assert Facteur([2, 3, 7]).nombre([1, 2]) == (2 ** 1) * (3 ** 2)
    assert Facteur([2, 3, 7]).nombre([1, 2, 3]) == (2 ** 1) * (3 ** 2) * (7 ** 3)


def test_Facteur_décomposition():
    assert Facteur([2, 3, 7]).décomposition(1) == [0, 0, 0]
    assert Facteur([2, 3, 7]).décomposition((2**3) * (3**2) * (7)) == [3, 2, 1]



def test_Fractran_init():
    fractions = [Fraction(17, 4), Fraction(12, 2)]
    fractran = Fractran(fractions)
    assert fractran.programme == fractions


def test_Fractran_run():
    fractions = [Fraction(3, 10), Fraction(4, 3)]
    fractran = Fractran(fractions)
    assert fractran.run(14) == 14
    assert fractran.run(15) == 8


def test_Fractran_suite():
    fractions = [Fraction(3, 10), Fraction(4, 3)]
    fractran = Fractran(fractions)
    assert fractran.suite(15, 5) == [15, 20, 6, 8]
    assert fractran.suite(15, 2) == [15, 20]