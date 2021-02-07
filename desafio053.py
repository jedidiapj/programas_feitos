#uma forma de fazer
'''frase = str(input('digite uma frase:\n')).lower().strip().split()
frase_junta = ''.join(frase)
frase_invert= frase_junta[::-1]

if frase_junta == frase_invert:
    print('é um palíndromo')
else:
    print('não é um palíndromo')

#print(frase_junta[::-1]) esse [] após a frase serve para tratamento de string [de onde começa, onde termina, intervalo]'''

# fazendo usando o for in
frase = str(input('digite uma frase:\n')).lower().strip()
frase_separada = frase.split()
frase_junta = ''.join(frase)
frase_invert= ''
for letra in range(len(frase_junta) -1, -1, -1):#
    frase_invert += frase_junta[letra]
if frase_junta == frase_invert:
    print('é um palíndromo')
else:
    print('não é um palíndromo')