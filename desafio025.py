nome_usuario = str(input('Digite seu nome completo:\n')).upper().strip()
achar_silva = 'SILVA' in nome_usuario

if achar_silva == True:
    print('Verdade')
else:
    print('Não encontrado')