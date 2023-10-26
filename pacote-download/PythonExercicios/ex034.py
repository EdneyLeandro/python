#Escreva um programa que leia o salário de um funcionário e calcule o
#valor do seu aumento. Para salários superiores a R$ 1250,00, calcule um
#aumento de 10%. Para os inferiores ou  iguais, o aumento é de 15%.

#Perguntando o salário...
salario = float(input('Salário: R$ '))

#Para salários superiores
if salario >= 1250:
    aumento = salario + (salario * 0.10)
    print(f'Aumento de 10%. Salário com aumento: R$ {aumento},00')
else:
    aumento = salario + (salario * 0.15)
    print(f'Aumento de 15%. Salário com aumento: R$ {aumento},00')
