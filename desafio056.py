#variaveis
soma = 0
id_maior = 0
nome_oldman = ''
totmulher20 = 0
# alimentando a base de dados
for b in range(1,5):
    print('---{}ª PESSOA---'.format(b))
    n = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip()
# calcular a média de idade do grupo
    soma += idade
    media_id = soma / b
 # calcular o homem mais velho e seu nome
    if b == 1 and sexo in 'Mm':
        id_maior += idade
        nome_oldman = n
    if sexo in 'Mm' and idade > id_maior:
        id_maior += idade
        nome_oldman = n
# numero de mulheres com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

print('A média de idade do grupo é {:.0f} anos'.format(media_id))
print('O homem mais velho tem {} anos e se chama {}'.format(id_maior, nome_oldman))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))