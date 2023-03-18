while True:
     y = int(input('the year:'))
     if y <= -11000:
          print('no a valid year')
          continue
     break
if y % 400 == 0:
    ly = y
elif y % 100 == 0:
    ly = -11001
elif y % 4 == 0:
    ly = y
else:
    ly = -11001
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
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d > 31 or d < 1:
            print('not a valid day')
            continue
        d = d2 + 1
    if d == 32:
        d = 1
        m = m2 + 1
        if m == 13:
            m = 1
            y2 = y
            y = y2 + 1
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if d > 30 or d < 0:
            print('not a valid day')
            continue
        d = d2 + 1
    if d == 31:
        d = 1
        m = m2 + 1
        if m == 13:
            m = 1
            y2 = y
            y = y2 + 1
    elif m == 2:
         if ly != y:
            if d > 28:
                 print('not a valid day')
                 continue
            d = d2 + 1
            if d == 29:
                d = 1
                m = m2 + 1
                if m == 13:
                    m = 1
                    y2 = y
                    y = y2 + 1
         elif y == ly:
            if d > 29:
                print('not a valid day')
                continue
            d = d2 + 1
            if d == 30:
                d = 1
                m = m2 + 1
                if m == 13:
                    m = 1
                    y2 = y
                    y = y2 + 1
    break
print('tomorow is ', y, '-', m, '-', d )