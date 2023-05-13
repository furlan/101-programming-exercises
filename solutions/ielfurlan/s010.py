thirty_one_days = [1, 3, 5, 7, 8, 10, 12]
thirty_days = [4, 6, 9, 11]
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
while True:
     y = int(input('the year:'))
     if y <= -11000:
          print('no a valid year')
          continue
     break
y2 = y
if y % 400 == 0:
    leap_year = y
elif y % 100 == 0:
    leap_year = -11001
elif y % 4 == 0:
    leap_year = y
else:
    leap_year = -11001
if leap_year == y:
    days[2] = 29
while True: 
    m = int(input('the month:'))
    if m > 12 or m < 1:
        print('not a valid month')
        continue
    m2 = m
    break
while True:
    d = int(input('the day:'))
    d2 = d
    if m in thirty_one_days:
        if d > 31 or d < 1:
            print('not a valid day')
            continue
    elif m in thirty_days:
        if d > 30 or d < 0:
            print('not a valid day')
            continue
    else:
         if leap_year != y:
            if d > 28:
                 print('not a valid day')
                 continue
         elif y == leap_year:
            if d > 29:
                print('not a valid day')
                continue
    break
d2 = d + 1
if d == days[m]:
    d2 = 1
    m = m2 + 1
    if m == 13:
        m = 1
        y = y2 + 1
print('tomorow is ', y, '-', m, '-', d2 )