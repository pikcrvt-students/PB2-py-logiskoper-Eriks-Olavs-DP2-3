import doctest
def parbaudit_koord(koord_x:float) -> bool:
    """
    Funkcijas parbaude x koordinati. xt(3.9; +inf)
    >>> parbaudit_koord(1.3)
    False
    >>> parbaudit_koord(3.9)
    False
    >>> parbaudit_koord(9)
    True

    """
    if koord_x > 3.9:
        return True
    else:
        return False

doctest.testmod(verbose=True)


vertiba = float(input('ievadiet x koordinati: '))
if parbaudit_koord(vertiba):
    print('Skaitlis ir diapazona')
else:
    print('Skaitlis NAV diapazona')