#Crie um programa que leia vários números inteiros e diga qual é o maior e o menor

#Inserindo os números...
num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro novamente: '))

#Procurando o maior...
if num > num2 and num > num3:
    print(f'{num} é o maior.')
elif num2 > num and num2 > num3:
    print(f'{num2} é o maior.')
else:
    print(f'{num3} é o maior.')

#Procurando o menor...
if num < num2 and num < num3:
    print(f'{num} é o menor.')
elif num2 < num and num2 < num3:
    print(f'{num2} é o menor.')
else:
    print(f'{num3} é o menor.')

#finalizando...
print('Fim do programa.')