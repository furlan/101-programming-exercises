year = int(input('enter the year: '))
if year % 400 == 0:
        print('year', year, 'is a leap year')
elif year % 100 == 0:
        print('year', year, 'is not a leap year')
elif year % 4 == 0:
        print('year', year, 'is a leap year')
else:
        print('year', year, 'is not a leap year')