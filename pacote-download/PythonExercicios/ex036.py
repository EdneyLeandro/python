#Escreva um programa para aprovar o empréstimo bancário para a compra de
# uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele
# vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input('Qual o valor da casa? '))
salario_comprador = float(input('Ok. E qual o seu salário? '))
anos_pagar = int(input('Em quantos anos pretende pagar? '))
prestacao = valor_casa/(anos_pagar*12)
print(prestacao)
if prestacao < (salario_comprador*0.3):
    print(f'Valor da casa: R$ {valor_casa}')
    print(f'Sua renda: R$ {salario_comprador}')
    print(f'{anos_pagar*12} parcelas')
    print(f'Valor das parcelas: R$ {prestacao}')
    print('Empréstimo aprovado.')
else:
    print(f'Valor da casa: R$ {valor_casa}')
    print(f'Sua renda: R$ {salario_comprador}')
    print(f'{anos_pagar * 12} parcelas')
    print(f'Valor das parcelas: R$ {prestacao}')
    print('Infelizmente não foi aprovado. Tente novamente daqui a 30 dias.')