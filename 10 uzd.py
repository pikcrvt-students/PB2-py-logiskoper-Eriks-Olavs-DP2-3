"""
Programma pārbauda punkta koordinates figurai, riņkim, riņķa centrs atrodas punkta 0,0, riņka radius 1 vieniba
"""
import doctest

from math import sqrt
def parbauditPunktaKoordinatas(x:float, y:float) -> int:
    """
    >>> parbauditPunktaKoordinatas(1, )
    3
    >>> parbauditPunktaKoordinatas(1, )
    3
    >>> parbauditPunktaKoordinatas(0,1)
    2
    >>> parbauditPunktaKoordinatas(-1,0)
    2
    >>> parbauditPunktaKoordinatas(0,-1)
    2
    >>> parbauditPunktaKoordinatas(1, 0)
    2
    >>> parbauditPunktaKoordinatas(0.5, 0.4)
    1
    >>> parbauditPunktaKoordinatas( )
    1
    >>> parbauditPunktaKoordinatas(0,0)
    1
    >>> parbauditPunktaKoordinatas()
    3
    >>> parbauditPunktaKoordinatas(0.7, ?)
    2
    """
    from math import sqrt
    if round(sqrt(x ** 2 + y ** 2), 1) <= 1:  # Pārbauda vai punkts atrodas figūras iekšā vai uz robežlīnijas.

        if round(sqrt(x ** 2 + y ** 2), 1) == 1:  # Pārbauda vai atrodas tieši uz robežlīnijas.
            return 2
        else:
            return 1
    else:
        return 3

doctest.testmod(verbose=True)

print("Ievadiet Dekarta plaknes koodrinātas līdz 2 cipariem aiz komata: ")
x = float(input("Ievadiet x koordinātu: "))
y = float(input("Ievadiet y koordinātu: "))

rezultats = parbauditPunktaKoordinatas(x, y)

if rezultats == 1:
    print("Punkts atrodas figūras iekšpusē.")

elif rezultats == 2:
    print("Punkts atrodas uz robežlīnijas.")

elif rezultats == 3:
    print("Punkts atrodas ārpus figūras.")