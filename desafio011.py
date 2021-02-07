alt = float(input('Qual a altura da parede:\n'))
larg = float(input('Qual a largura da parede?\n'))
area = alt*larg
tinta = area/2

print("""Sua parede tem: {} de altura e {} de largura.'
Logo tem {} metros quadrados.
Precisamos de {:.2f}L de tinta para pintar""".format(alt, larg, area, tinta))
