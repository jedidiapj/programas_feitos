valor = float(input('Digite o valor a ser pago: \nR$ '))
avista = float(valor-(valor*(10/100)))
avista_cartao = float(valor-(valor*(5/100)))
cartao2x = valor
cartao3x = float(valor + ((valor * (20 / 100))))

print('''Escolha uma forma de pagamento:
[ 1 ] À vista - 10% desconto
[ 2 ] À vista no cartão - 5% desconto
[ 3 ] 2x no cartão sem juros
[ 4 ] Parcelado com juros''')
opcao = int(input('Sua escolha: '))

if opcao == 1:
    print('''A forma de pagamento escolhida foi À vista.
O valor a ser pago é: R${:.2f}'''.format(avista))
elif opcao == 2:
    print('''A forma de pagamento escolhida foi À vista no cartão. 
O valor a ser pago é: R${:.2f}'''.format(avista_cartao))
elif opcao == 3:
    parcelas = cartao2x/2
    print('''A forma de pagamento escolhida foi em 2x sem juros. 
O valor a ser pago é: 2x R${:.2f}'''.format(parcelas))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    total_parcela = cartao3x / parcelas
    print('''A forma de pagamento escolhida foi em {}x de R${:.2f} COM JUROS. 
O valor a ser pago é: R${}'''.format(parcelas, total_parcela,cartao3x ))
else:
    print('Opção inválida, por gentileza escolher novamente a forma de pagamento')

