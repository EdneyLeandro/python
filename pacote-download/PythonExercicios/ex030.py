#Crie um programa que leia um número inteiro e diga se ele é par ou ímpar

num = int(input('Digite um número: '))
if num%2 == 0:
    print(f'Você digitou {num}. Este número é par!')
else:
    print(f'Você digitou {num}. Este número é ímpar!')