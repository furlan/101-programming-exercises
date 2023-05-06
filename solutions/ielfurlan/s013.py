b = []
c = 0
while True:
    a = int(input('the number:'))
    if a != 0:
        b.append(a)
        c = c + a
    else:
        break
if c == 0:
    print('error: 0 cannot be the first number')
else:
    d = len(b)
    e = c/d
    print('the average is', e)