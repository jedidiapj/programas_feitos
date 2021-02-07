n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero: [999 para parar]: '))
    soma += n
    soma_final = soma - 999
    cont += 1

print('''\nvoce digitou {} vezes até parar
A soma dos números digitados é de: {}'''.format(cont, soma_final))
