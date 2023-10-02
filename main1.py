import doctest
def parb(x):
    """
    >>> parb(10)
    Ir intervala
    >>> parb(-2)
    Ir intervala
    >>> parb(3,9)
    Nav intervala
    """


x = int(input('x:'))

if x > 10 and x < 50:
    print('True')
else:
    print('False')