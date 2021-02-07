frase = str(input('Digite uma frase:\n')).upper().strip()

#a = frase.count('A') conta quantos a tem na frase
#a_primeiravez = frase_upper.find('A'+1) # apresenta a primeira posição de a
#a_ultimavez = frase_upper.rfind('A'+1)

print('A letra A aparece {} na frase.\n'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}\n'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}\n'.format(frase.rfind('A')+1))

