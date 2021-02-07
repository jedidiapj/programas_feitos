nome = input('Digite seu nome completo:\n')
nome_dividido = nome.split()
contar_nome = len(nome_dividido)
nome_junto = len(''.join(nome_dividido)) #contar quantas letras tem o nome sem espaço
primeiro_nome = len(nome_dividido[0])


#print(len(nome))24 letras
#print(nome_dividido)
#print(contar_nome)
#print(nome_junto)
#print(primeiro_nome)

print('seu nome maiusculo fica:\n{}\n'.format(nome.upper()))
print('seu nome minusculo fica:\n{}\n'.format(nome.lower()))
print('seu nome tem {} letras\n'.format(nome_junto))
print('Seu primeiro nome tem {} letras'.format(primeiro_nome))


# não conseguir fazer o programa interagir segundo a resposta do usuário
'''condição_1 = input('Gostaria de ver seu nome em MAIUSCULO?\n')

if condição_1 == True:
    print(nome.upper())'''
