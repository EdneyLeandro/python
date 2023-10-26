vel = float(input('Qual a sua velocidade? '))
multa = 7 * (vel - 80)
if vel <= 80:
    print('Você está dentro do limite permitido.')
else:
    print(f"""O limite máximo permitido é de 80km/h. 
Você está sendo multado e deve pagar uma taxa de R$ {multa}.""")
print('Continue com segurança.')