num1 = float(input('Digite um numero:\n'))
num2 = float(input('Digite um numero:\n'))
num3 = float(input('Digite um numero:\n'))

menor = num1

if num2 < num1 and num3 > num2:
    menor = num2
if num3 < num1 and num2 > num3:
    menor = num3

maior = num1

if num2 > num1 and num3 < num2:
    maior = num2
if num3 > num1 and num2 < num3:
    maior = num3

print('O menor valor digitado foi {}\n'.format(menor))
print('o maior valor digitado foi {}\n'.format(maior))
