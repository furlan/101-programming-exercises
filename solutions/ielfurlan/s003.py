a = int(input('the value of a is: '))
b = int(input('the value of b is: '))
option = input('add or sub or mul or div: ')
if option == 'add':
    c = a + b
    print('adding a and b is', c)
elif option == 'sub':
    c = a - b
    print('subtracting a and b is', c)
elif option == 'mul':
    c = a * b
    print('multiplying a and b is', c)
elif option =='div':
    if b == 0:
        print('don\'t divide by 0, ok?')
    else:
        c = a/b
        print('dividing a and b is', c)
else:
    print('no')