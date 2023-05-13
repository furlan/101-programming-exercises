lp = input('license plate (no spaces):')
if lp[0].isalpha() and lp[1].isalpha() and lp[2].isalpha() and lp[3].isdigit() and lp[4].isdigit() and lp[5].isdigit:
    if lp[0].isupper() and lp[1].isupper() and lp[2].isupper():
        print(lp, 'is an old license plate')
    else:
        print('all uppercase only')
elif lp[0].isdigit() and lp[1].isdigit() and lp[2].isdigit() and lp[3].isdigit() and lp[4].isalpha() and lp[5].isalpha and lp[6].isalpha():
    if lp[4].isupper() and lp[5].isupper() and lp[6].isupper():
        print(lp, 'is a new license plate')
    else:
        print('all uppercase only')
else:
    print(lp, 'is not a valid lisence plate yet')