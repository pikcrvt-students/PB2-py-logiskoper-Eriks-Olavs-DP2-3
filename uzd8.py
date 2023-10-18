x = int(input('Ievadiet x koordinatus: '))
y = int(input('Ievadiet y koordinatus: '))

if x >= -5 and x <= 2 and y >= -1 and y <= 3:
    if y == -1 and x >= -5 and x <= 2 or y == 3 and x >= -5 and x <= 2 or x == -5 and y >= -1 and y<=3 or x == 2 and y >= -1 and y<=3:
        print('Skaitli ir figuras mala')
    else:
        print('Skaitlis ir figura')
else:
    print('skaitlis nav figura')