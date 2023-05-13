a = input('Uppercase and lowercase matters. Put your word here: ')
b = ''.join(reversed(a))
if a == b:
    print(a, 'Is a palindrome')
else:
    print(a, 'Is not a palindrome')