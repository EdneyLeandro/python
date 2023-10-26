frase = str(input('Digite uma frase: ')).strip().upper()
a = frase.count('A')
print(f'Tem {a} letra(s) "a" na frase.')
b = frase.find('A')+1
print(f'A primeira letra "a" está na posição {b}.')
c = frase.rfind('A')+1
print(f'A última letra "a" está na posição {c}.')
