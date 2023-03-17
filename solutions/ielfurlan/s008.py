while True:
    a = int(input('a = '))
    if a == 0:
        print('a != 0')
        continue
    break
b = int(input('b = '))
c = int(input('c = '))
delta = b**2 - (4*a*c)
if delta < 0:
    print('no real roots')
elif delta == 0:
    print('1 real root')
    x = -b/(2*a)
    print('x =', x)
elif delta > 0:
    print('2 real roots')
    print('x1 = the equation with the addition sign')
    print('x2 = the equation with the subtraction sign')
    import math
    d = math.sqrt(delta)
    x1 = (-b + d)/(2*a)
    x2 = (-b - d)/(2*a)
    print('x1 =', x1)
    print('x2 =', x2)