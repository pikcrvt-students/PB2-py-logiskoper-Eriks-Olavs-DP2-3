import doctest


def checkcoord(x: float, y: float) -> int:
    """
    >>> checkcoord(-2.5, 5)
    1
    >>> checkcoord(4, 5)
    1
    >>> checkcoord(6, 4)
    1
    >>> checkcoord(8.2, 2)
    2
    >>> checkcoord(0, 2)
    2
    >>> checkcoord(3, 8)
    2
    >>> checkcoord(7.5, 3)
    2
    >>> checkcoord(-3, 2)
    2
    >>> checkcoord(-2, 8)
    2
    >>> checkcoord(4, 8)
    2
    >>> checkcoord(-4, 7)
    3
    >>> checkcoord(6, 6)
    3
    >>> checkcoord(-2.75, 5)
    2
    >>> checkcoord(-2.9, 3.2)
    2
    >>> checkcoord(5, 6.57)
    2
    >>> checkcoord(5, 6.57)
    2
    >>> checkcoord(6, 5.14)
    2
    >>> checkcoord(5.4, 6)
    2
    """


    kreisapuse = round(12 * x + 38, 2)

    koef = -6 / 4.2
    b = 2 - koef * 8.2
    labapuse = round(koef * x + b, 2)

    if x >= -2.5 and x <= 4 and y >= 2 and y <= 8:

        if y == 2 or y == 8:
            return 2
        else:
            return 1

    elif x <= -2.5 and y >= 2 and y <= kreisapuse:

        if y == 2 or x == -2.5 or y == kreisapuse:
            return 2
        else:
            return 1

    elif x >= 4 and y >= 2 and y <= labapuse:

        if y == 2 or x == 4 or y == labapuse:
            return 2
        else:
            return 1

    else:
        return 3


doctest.testmod(verbose=True)

print("ievadiet koordinati ar 2 cipariem aiz komata ")
x = float(input("Ievadiet x: "))
y = float(input("Ievadiet y: "))

rezultats = checkcoord(x, y)

if rezultats == 1:
    print("Punkts atrodas figūras iekšpusē.")

elif rezultats == 2:
    print("Punkts atrodas uz robežlīnijas.")

elif rezultats == 3:
    print("Punkts atrodas ārpus figūras.")