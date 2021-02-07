# usando string ocorre um erro no programa caso seja utilizado um numero sem 4 digitos
'''numero = int(input('Digite um numero entre 0 e 9999\n'))
n= str(numero)

#print(numero_dividido)

print('unidade: {}\n'.format(n[3]))
print('dezenas: {}\n'.format(n[2]))
print('centenas: {}\n'.format(n[1]))
print('milhar: {}\n'.format(n[0]))'''

# forma matemática de se resolver
numero = int(input('Digite um numero entre 0 e 9999\n'))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('unidade: {}\n'.format(u))
print('dezenas: {}\n'.format(d))
print('centenas: {}\n'.format(c))
print('milhar: {}\n'.format(m))