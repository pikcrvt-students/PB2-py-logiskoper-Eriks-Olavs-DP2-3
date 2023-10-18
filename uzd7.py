x = int(input('Ievadiet x koordinatus: '))
y = int(input('Ievadiet y koordinatus: '))

if x >= -1 and x <= 3 and y >= -2 and y <= 1:
    print('Skaitlis ir figura')
elif y == -2 and x >= -1 and x <= 3 or y == 1 and x >= -1 and x <= 3 or x == -1 and y >= -2 and y<=1 or x == 3 and y >= -2 and y<=1:
    print('Skaitli ir figuras mala')
else:
    print('skaitlis nav figura')