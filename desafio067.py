n = cont = 0
opcao = ''

while True:
    n = int(input('Quer ver a tabuada de que número? '))
    for c in range(0, 11):
        if n > 0:
            print(f'''{n} x {c} = {n*c}''')
        else:
            break
    if n < 0:
        opcao = str(input('Valor incorreto. Gostaria de escolher outro número? ')).upper().strip()
        if opcao in 'SIM,S':
            continue
        else:
            break
print('Obrigado por usar nosso programa')