import doctest

def uzd13(x: float, y: float):
    """
    >>> uzd13(-4,0)
    1
    >>> uzd13(4,0)
    3
    >>> uzd13(-3,1.5)
    1
    >>> uzd13(-2,3)
    1
    >>> uzd13(-1,3)
    1
    >>> uzd13(0,0)
    2
    >>> uzd13(1,1)
    2
    >>> uzd13(0,-2)
    1
    >>> uzd13(2.4,1.2)
    1
    >>> uzd13(3, 3)
    3
    >>> uzd13(5, 5)
    3
    >>> uzd13(0, 2)
    1
    >>> uzd13(-4, 0)
    2
    """
    f1 = round(1.5*x+6, 3)
    f2 = round((-5/3)*x-(20/3), 3)
    f3 = round(-2*x+6, 3)
    if x <= 4 and x >= -4 and y <= 3 and y >= -2 and y <= f1 and y >= f2 and y <= f3:
        if y == -2 or y == 3 or y == f1 or y == f2 or y == f3:
            print("1")
        else:
            print("2")
    else:
        print("3")

doctest.testmod(verbose=True)

x = float(input("X: "))
y = float(input("Y: "))

uzd13(x,y)