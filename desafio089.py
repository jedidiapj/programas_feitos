boletim = list()
inf_alunos = list()
nome = list()
notas = list()
media = []
medias = []
titulo = '\033[1mBOLETIM\033[m'
while True:
    nome.append(str(input('Digite o nome do aluno: ')))
    for n in range(0,2):
        num = (float(input(f'Digite {n+1}ª nota: ')))
        notas.append(num)
        media.append(num)
    soma = (media[0] + media[1]) / 2
    medias.append(soma)
    media.clear()
    inf_alunos.append(nome[:])
    inf_alunos.append(notas[:])
    inf_alunos.append(medias[:])
    notas.clear()
    nome.clear()
    medias.clear()
    boletim.append(inf_alunos[:])
    inf_alunos.clear()
    sair = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if sair in 'S,SIM':
        continue
    else:
        break

print()
print('-=-'*11)
print(f'{titulo:-^40}')
print('-=-'*11)
print(f'{"No.":<4}{"NOME":<12}{"MÉDIA":>4}')
print('-'*33)


for i, l in enumerate(boletim):
    print(f'{i:<4}{l[0]}       {l[2]}')
while True:
    print('-'*35)
    m = int(input('Mostrar a nota de qual aluno? (999 interrompe) '))
    if m <= len(boletim)-1:
        print(f'as notas de {boletim[m][0]} são {boletim[m][1]}')
        continue
    if m == 999:
        break
