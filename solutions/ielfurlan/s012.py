from random import randint
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
s = randint(0,37)
if s == 37:
    s = 00
print('the spin resulted in', s, '...')
print('pay', s)
if s != 0 and s != 00:
    if s in red:
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
else:
    print('pay,', s)