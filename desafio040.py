nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

print('\nTirando {} e {} a média do aluno é {}\n'.format(nota1, nota2, media))
if media < 5:
    print('Você está reprovado')
elif media < 7:
    print('Você está de recuperação')
else:
    print('Você está aprovado')