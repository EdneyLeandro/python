#Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 1 para binário,
# 2 para octal e 3 para hexadecimal.
print('Como deseja converter seu número? ')
print('[ 1 ] Binario')
print('[ 2 ] Octal')
print('[ 3 ] Hexadecimal')
escolha = int(input(' '))
if escolha == 1:
    num = int(input('Ok, digite um número inteiro: '))
    print(f'{num} em binário: {bin(num) [2:]}')
elif escolha == 2:
    num = int(input('Ok, digite um número inteiro: '))
    print(f'{num} em octal: {oct(num) [2:]}')
elif escolha == 3:
    num = int(input('Ok, digite um número inteiro: '))
    print(f'{num} em hexadcimal: {hex(num) [2:]}')
else:
    print('Opção inválida.')
print('FIM')