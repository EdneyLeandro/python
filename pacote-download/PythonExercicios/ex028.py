from random import randint

computador = randint(0, 5)
questao = int(input('De 0 a 5, em que número estou pensando? '))
if questao == computador:
    print('Parabéns você acertou!')
else:
    print(f'Você perdeu...eu pensei no número {computador}')
print('Até mais!!')
