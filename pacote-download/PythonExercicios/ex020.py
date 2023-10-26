import random

n1 = input('Nome: ')
n2 = input('Nome: ')
n3 = input('Nome: ')
n4 = input('Nome: ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem é: ')
print(lista)