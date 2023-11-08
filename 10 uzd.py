
import doctest

from math import sqrt
def parbauditPunktaKoordinatas(x:float, y:float) -> int:
    """
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
    >>> parbauditPunktaKoordinatas(0,0)
    1
    """
    from math import sqrt
    if round(sqrt(x ** 2 + y ** 2), 1) <= 1:

        if round(sqrt(x ** 2 + y ** 2), 1) == 1:
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