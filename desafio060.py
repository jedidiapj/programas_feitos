from math import factorial
num = int(input('digite um numero: '))
c = num
f = factorial(num)
while c > 0:
    if c > 1:
        print('{} x '.format(c), end='')
    elif c == 1:
        print('{} = {:.2f}'.format(c,f), end='')
    c -= 1


