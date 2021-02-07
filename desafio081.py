valores = []
while True:
    n = int(input(f'Digite um número: '))
    valores.append(n)
    sair = str(input('Deseja continuar? [S/N]')).upper().strip()
    if sair in 'N,NÃO':
        break
print(f'Foram digitados {len(valores)} números')
valores.sort(reverse=True)
print(valores)
if 5 not in valores:
    print('O valor 5 não foi adicionado à lista.')
else:
    print(f'Numero 5 adicionado {valores.count(5)} vezes')
