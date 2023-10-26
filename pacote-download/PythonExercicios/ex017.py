from math import pow, sqrt

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
c = pow(co,2) + pow(ca,2)

print('A hipotenusa vale {}'.format(sqrt(c)))
