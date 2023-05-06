from random import randint
s = randint(0,37)
if s == 37:
    s = 00
print('the spin resulted in', s, '...')
print('pay', s)
if s != 0 and s != 00:
    if s == 1 or s == 3 or s == 5 or s == 7 or s == 9 or s == 12 or s == 14 or s == 16 or s == 18 or s == 19 or s == 21 or s == 23 or s == 25 or s == 27 or s == 30 or s == 32 or s == 34 or s == 36:
        print('pay red')
    else:
        print('pay black')
    if (s % 2) == 0:
        print('pay even')
    else:
        print('pay odd')
    if s >= 1 and s <= 18:
        print('pay 1-18')
    else:
        print('pay 19-36')