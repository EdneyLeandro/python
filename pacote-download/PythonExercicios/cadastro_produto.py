#lista vazia. Será preenchida através do comando .append
produtos = []
#função para retornar o valor das listas do dicionário
def cadastramento(produto_cadastrado: dict):
    produtos.append(produto_cadastrado)
    return
#enquanto a opção de cadastro for igual a 1(um), um produto novo será
#acrescentado a lista. Caso contrário o cadastro é encerrado.
print('Realizar cadastro?')
cadastro = int(input('[ 1 ] Sim [ 0 ] Não '))
while cadastro == 1:
    lançamento = {}
    lançamento['codigo'] = int(input('Insira o código: '))
    if lançamento['codigo'] == 0:
        print('Finalizando cadastro...')
        break
    lançamento['estoque'] = int(input('Quantidade em estoque: '))
    lançamento['minimo'] = int(input('Quantidade mínima do estoque:'))
    cadastramento(lançamento)
    print('Realizar cadastro?')
    cadastro = int(input('[ 1 ] Sim [ 0 ] Não '))
#Os produtos são listados em ordem crescente
if len(produtos) > 0:
    print('Códigos em ordem crescente: ')
    print("Código".center(12), end='')
    print("Estoque".center(12), end='')
    print("Mínimo".center(12))
    for produto in sorted(produtos, key=lambda item: item['codigo']):
        print(str(produto['codigo']).center(12), end='')
        print(str(produto['estoque']).center(12), end='')
        print(str(produto['minimo']).center(12))
#Caso não haja cadastramento, o programa retornará o aviso de lista vazia
else:
    print('Vazio')