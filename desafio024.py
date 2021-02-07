nome_cidade = str(input('Digite o nome da sua cidade:\n')).upper().strip().split()
achar_santo = 'SANTO' in nome_cidade[0]

if achar_santo == True:
    print('Verdade')
else:
    print('Falso')

