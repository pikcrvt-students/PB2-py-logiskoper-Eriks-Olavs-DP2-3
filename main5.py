import doctest
def parbaudit_koord(koord_x:float) -> bool:
    """
    Funkcijas parbaude x koordinati.
    >>> parbaudit_koord(-3)
    False
    >>> parbaudit_koord(5)
    False
    >>> parbaudit_koord(-2)
    True
    """
    if koord_x >= -2 and koord_x < 5:
        return True
    else:
        return False
doctest.testmod(verbose=True)


vertiba = float(input('ievadiet x koordinati: '))
if parbaudit_koord(vertiba):
    print('Skaitlis ir diapazona')
else:
    print('Skaitlis NAV diapazona')