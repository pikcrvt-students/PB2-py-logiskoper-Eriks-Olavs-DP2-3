x = float(input('ievadiet x koordinati:'))
y = float(input('ievadiet y koordinati:'))

if (0 <= x <= 2) or (0 <= y <= 3):
    if (x == 0 and (0 <= y <= 3)) or (y == 0 and 0 <= x <= 2) or y == -1.5 * x + 3 and 0 < x < 2:
        print('Punkts ir robežas līnijā')
else:
    print('Punkts ir figuras iekšā')
