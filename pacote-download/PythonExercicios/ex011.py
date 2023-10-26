h = float(input('Qual a altura da parede (em metros)? '))
l = float(input('Qual a largura da parede? '))
m2 = h*l
lt = m2/2
print('Dimensão: {}x{}m'.format(h,l))
print('Área total: {:.2f}m²'.format(m2))
print('Litros de tinta necessários: {:.2f}l.'.format(lt))
