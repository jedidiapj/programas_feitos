def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric() == True:
            r = print(f'O valor digitado foi {n}')
            return r
        else:
            print(f'\033[31mDigite um valor válido\033[m')


#programa principal
n = leiaint('Digite um numero inteiro: ')