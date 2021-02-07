valores = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    if n % 2 == 1:
        impar.append(n)
    sair = str(input('Deseja continuar? [S/N]')).upper().strip()
    if sair in 'N,NÃO':
        break
print(valores)
print(sorted(par))
print(sorted(impar))
#outra forma de fazer:
'''for i, v in enumerate(valores):#analisa os valores que já estão dentro da lista
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)'''
