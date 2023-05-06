a = input('Uppercase and lowercase matters. Put your word here: ')
b = a[::-1]
if a == b:
    print(a, 'Is a palindrome')
else:
    print(a, 'Is not a palindrome')