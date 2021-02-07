sexo = ''
while sexo == 'M' or 'F':
    sexo = str(input('Qual seu sexo? [M/F]: ').upper())
    if sexo != 'M' and sexo != 'F':
        print('Digite uma resposta válida')

