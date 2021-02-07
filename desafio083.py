from time import sleep
expr = str(input('Digite uma expressão: '))
pilha = []
for simb in expr:#verifica na expressão os simbolos
    if simb == '(':# quando encontra um ( na expressão adiciona na lista
        pilha.append('(')
        print(pilha)
        sleep(1.5)
    elif simb == ')':#caso encontre um fechando
        if len(pilha) > 0: #apaga o ultimo até chegar a 0
            pilha.pop()
            print(pilha)
            sleep(1.5)
        else: # depois que chegar a 0 ele adiciona os ) que estão sem "par"
            pilha.append(')')
            print(pilha)
            sleep(1.5)
            break
if len(pilha) == 0:
    print('Expressão válida')
else:
    print('expressão inválida')