while True:
    a = int(input('a = '))
    if a == 0:
        print('a != 0')
        continue
    break
b = int(input('b = '))
c = int(input('c = '))
if b*b-4*a*c < 0:
    print('no real roots')
elif b*b-4*a*c == 0:
    print('1 real root')
    x = -b/(2*a)
    print('x =', x)
elif b*b-4*a*c > 0:
    print('2 real roots')
    print('x1 = the equation with the addition sign')
    print('x2 = the equation with the subtraction sign')
    import math
    d = math.sqrt(a)
    e = math.sqrt(c)
    x1 = (-b + (b - 2*d*c))/(2*a)
    x2 = (-b - (b - 2*d*c))/(2*a)
    print('x1 =', x1)
    print('x2 =', x2)