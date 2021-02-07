numeros = []
par = []
impar = []
for p in range(0,7):
    num = int(input(f'Digite o {p+1}º Valor: '))
    if num % 2 == 0:
        par.append(num)
    elif num % 2 == 1:
        impar.append(num)
numeros.append(sorted(par)[:])
numeros.append(sorted(impar)[:])

#print(sorted(par))
#print(sorted(impar))
print(numeros[0])
print(numeros[1])