km = float(input('Km rodados: '))
dias = int(input('Dias alugados: '))
vd = dias*60
vkm = km*0.15
vt = vd+vkm
print('Valor a pagar: R$ {}'.format(vt))
