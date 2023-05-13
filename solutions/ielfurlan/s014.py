a = float(input('the money input: '))
b = a//100
d = a % 100
e = d//50
g = d % 50
h = g//10
j = g % 10
if j < 10 and j > 0:
    print('sorry, our smallest bill is the ten dollar bill')
else: 
    print('you get', b, 'one hundred dollar bills(s),', e, 'fifty dollar bill(s),', h, 'ten dollar bill(s),')