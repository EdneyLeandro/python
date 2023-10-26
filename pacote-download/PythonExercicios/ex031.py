#Desenvolva um programa que pergunte a distância de uma viagem em
# km. Calcule o preço da passagem cobrando R$ 0,50 por Km para viagens
# de até 200Km e R$ 0,45 para viagens mais longas.

#Inserindo a distância...
d = float(input('Qual a distância da sua viagem (Km)? '))

#Calculando o valor...
if d <= 200:
    preco = d * 0.5
    print(f'A sua passagem fica em R$ {preco}')
else:
    preco = d * 0.45
    print(f'A sua passagem fica em R$ {preco}')
