#Exercício Python 035: Desenvolva um programa que leia o comprimento de
# três retas e diga ao usuário se elas podem ou não formar um triângulo.
#REGRA: Cada segmento tem que ser menor do que a soma dos outros 02 segmentos.

r1 = int(input('Reta 01: '))
r2 = int(input('Reta 02: '))
r3 = int(input('Reta 03: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
