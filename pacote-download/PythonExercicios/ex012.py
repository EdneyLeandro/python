preco = float(input('Qual o preço do produto? R$ '))
desconto = preco*0.05
pd = preco - desconto
print('Valor com desconto de 5%: R$ {:.2f}.'.format(pd))
