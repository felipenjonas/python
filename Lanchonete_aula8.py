# 2) Escrever um programa em python que leia o código
# do produto escolhido do cardápio de uma lanchonete
# e a quantidade. O programa deve calcular o valor a ser
# pago por aquele lanche. Considere que a cada
# execução somente será calculado um pedido. O
# cardápio da lanchonete segue o padrão abaixo:

from tabulate import tabulate

print('\nBem vindo!')
print()
print('Menu da lanchonete: ')


def line():
    print('-'*30)


print (tabulate([['Cachorro Quente', 100,1.20], ['Bauru Simples', 101,1.30],['Bauru com ovo',102,1.50],['Hamburguer',103,1.20],['Cheeseburguer',104,1.70],['Suco',105,1.20],['Refrigerante',106,1.00]], headers=['Especificacao', 'Codigo','Preço']))
line()


while(True):
    line()
    codigo = (int(input('\nDigite o código do produto escolhido: ')))
    
    if(codigo <= 99 or codigo >= 107):
        line()
        print('\nProduto não existe no menu')
        line()
    if(codigo == 100):
        quantidade = (int(input('Digite a quantidade do produto: ')))
        line()
        total = quantidade * 1.20
        # f como string substitui o .format permitindo qualquer ação dentro de {}
        # :.2f possibilita a precisao de 2 casas decimais no calculo
        print('Produto: Cachorro-Quente')
        print(f'Quantidade: {quantidade}')
        print(f'\nValor total a ser pago: R${total:.2f}')
    if(codigo ==101):
        quantidade = (int(input('Digite a quantidade do produto: ')))
        line()
        total = quantidade * 1.30
        print('Produto: Bauru Simples')
        print(f'Quantidade: {quantidade}')
        print(f'\nValor total a ser pago: R${total:.2f}')
    if(codigo ==102):
        quantidade = (int(input('Digite a quantidade do produto: ')))
        line()
        total = quantidade * 1.50
        print('Produto: Bauru com ovo')
        print(f'Quantidade: {quantidade}')
        print(f'\nValor total a ser pago: R${total:.2f}')
    if(codigo ==103):
        quantidade = (int(input('Digite a quantidade do produto: ')))
        line()
        total = quantidade * 1.20
        print('Produto: Hamburguer')
        print(f'Quantidade: {quantidade}')
        print(f'\nValor total a ser pago: R${total:.2f}')
    if(codigo ==104):
        quantidade = (int(input('Digite a quantidade do produto: ')))
        line()
        total = quantidade * 1.70
        print('Produto: Cheeseburguer')
        print(f'Quantidade: {quantidade}')
        print(f'\nValor total a ser pago: R${total:.2f}')    
    if(codigo ==105):
        quantidade = (int(input('Digite a quantidade do produto: ')))
        line()
        total = quantidade * 1.20
        print('Produto: Suco')
        print(f'Quantidade: {quantidade}')
        print(f'\nValor total a ser pago: R${total:.2f}')
    if(codigo ==106):
        quantidade = (int(input('Digite a quantidade do produto: ')))
        line()
        total = quantidade * 1.00
        print('Produto: Refrigerante')
        print(f'Quantidade: {quantidade}')
        print(f'\nValor total a ser pago: R${total:.2f}')
    