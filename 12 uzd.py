import doctest


def koord(x, y: float) -> int:
    """
    >>> koord(-1, -1)
    2
    >>> koord(3, 3)
    3
    >>> koord(5, 5)
    3
    >>> koord(2, -1)
    1
    >>> koord(1, 1)
    2
    >>> koord(2, 2)
    """

    r = 2
    attalums = ((x + 4) ** 2) + ((y - 3) ** 2)

    if attalums <= r:
        if attalums == r:
            return 2
        else:
            return 1
    else:
        return 3


doctest.testmod(verbose=True)
vertibax = float(input("Ievadiet x: "))
vertibay = float(input("Ievadiet y: "))

a = koord(vertibax, vertibay)

if a == 2:
    print("Punkts ir uz robežas")
elif a == 1:
    print("Punkts ir figūrā")
elif a == 3:
    print("Punkts nav figūrā")
