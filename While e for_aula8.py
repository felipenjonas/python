# 4) Faça um programa em python que escreva na tela,
# de 1 até 100, de 1 em 1, usando a estrutura de
# repetição while e de 100 até 1 , de 1 em 1, usando a
# estrutura de repetição for.

def line():
    print('-'*30)

print('\n\tPara usar [while], digite [1]: ')
print('\n\tPara usar [For], digite [2]: ')
opcao = (input('\n'))
line()
if(opcao =='1'):
    a = 0
    while(True):
        a += 1
        print('\n\t\t{}'.format(a))
        if(a == 100):
            break
if(opcao == '2'):
    for numero in range(100,0,-1):
        print('\n\t\t{}'.format(numero)) 