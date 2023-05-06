a = float(input('the money input: '))
b = a/100
c = int(b)
d = a % 100
e = d/50
f = int(e)
g = d % 50
h = g/10
i = int(h)
j = g % 10
if j < 10 and j > 0:
    print('sorry, our smallest bill is the ten dollar bill')
else: 
    print('you get', c, 'one hundred dollar bills(s),', f, 'fifty dollar bill(s),', i, 'ten dollar bill(s),')