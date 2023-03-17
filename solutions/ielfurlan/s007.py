column = input('put the column of the square: ')
if column == 'a' or  column == 'c' or column == 'e' or column == 'g':
    column = 1
elif column == 'b' or column == 'd' or column == 'f' or column == 'h':
    column = 0
else:
    print('a-h only, person')
row = input('put the row of the square: ')
if row == '1' or row == '3' or row == '5' or row == '7':
    row = 1
elif row == '2' or row == '4' or row == '6' or row == '8':
    row = 0
else:
    print('1-8 only, person')
square = row + column
if square == 0 or square == 2:
    square = 'black'
elif square == 1:
    square = 'white' 
print('The color of the square is:', square)