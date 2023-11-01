x = float(input('ievadiet x koordinati:'))
y = float(input('ievadiet y koordinati:'))

if (-1 <= x <= 2) or (0 <= y <= 4):
    if (x == -1 and (0 <= y <= 4)) or (y == 0 and -1 <= x <= 2) or y == -1.5 * x + 3 and -1 < x < 2:
        print('Punkts ir robežas līnijā')
else:
    print('Punkts neatrodas figura')
