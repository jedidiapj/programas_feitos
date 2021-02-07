carteira = float(input('Quanto você tem na carteira\nR$'))

cambio = carteira//3.27

print('Com R${:.2f} você consegue comprar ${:.2f} '.format(carteira, cambio))
