nome_usuário = str(input('Digite seu nome completo:\n')).strip()
nome_divido = nome_usuário.split()

# o range de uma lista começa no -1
print('Seu primeiro nome é {}\n'.format(nome_divido[0]))
print('Seu ultimo nome é {}\n'.format(nome_divido[len(nome_divido)-1]))
