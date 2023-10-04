import doctest
def parbaudit_koord(koord_x:float):
    """
    Funkcija pārbauda x koordināti . x pieder (3.9;+ infinit
    >>> parbaudit_koord(3)
    False
    >>> parbaudit_koord(-1)
    False
    >>> parbaudit_koord(7)
    True
    """
    if koord_x > 3.9:
        return True
    else:
        return False

if __name__ == '__main__':
    doctest.testmod(verbose=True)

    vertiba = float(input("Ievadiet x koordināti: "))

    if parbaudit_koord(vertiba):
        print("Skaitlis ir diapazonā")
    else:
        print("Skaitlis nav diapazonā")