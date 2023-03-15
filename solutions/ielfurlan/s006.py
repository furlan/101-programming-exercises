famlist = []
a = int(1)
while True:
    print('Enter name of family member', a )
    b = input()
    a = a + 1
    if b == ' ':
        break
    famlist.append(b)
a = a - 2
for c in range(0, 100 * a, a):
    for d in range(1, a + 1):
        print(c + d, '-', famlist[0])
        famlist.append(famlist[0])
        del famlist[0]