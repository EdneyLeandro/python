#Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

num01 = int(input('Digite um número inteiro: '))
num02 = int(input('Digite outro número inteiro: '))
if num01 > num02:
    print(f'{num01} é maior.')
elif num02 > num01:
    print(f'{num02} é maior.')
else:
    print('Não existe maior ou menor. Os dois números são iguais.')
print('FIM')