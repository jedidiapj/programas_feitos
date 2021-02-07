palavra = opcao = ''
#define o local para colher os dados
while True:
    palavra = str(input('Digite uma palavra: '))
    print(f'Na palavra {palavra} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    opcao = str(input('\nDeseja continuar? [S/N]: ')).upper().strip()
    if opcao in 'S,SIM':
        continue
    else:
        break