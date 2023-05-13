a = 3
for b in range(1,9):
     e = (b-1)*4
     c = 4+e
     d = (2+e)*(3+e)*c
     a = a + (4/d)
     print(a)  
     if b == 8:
          break
     f = c*(5+e)*(6+e)
     a = a-(4/f)
     print(a)