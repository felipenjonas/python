# Leia o salário de um trabalhador e o valor da
# prestação de um empréstimo. Se a prestação for
# maior que 20% do salário imprima: Empréstimo não
# concedido, caso contrário imprima: Empréstimo
# concedido.
print('\n\t\t\t --Validador de Empréstimos--\n\n ')
cancela = "000"
continua = '1'

def line():
    print('-'*30)


while(continua == "1"):
    
    
    salario = (float(input('\nSalário: ')))

    prestacao =(float(input('\nValor da prestação: ')))
    
    calcula = salario * 0.2

    if(prestacao > calcula ):
        line()
        print('\nEmpréstimo não concedido')
        line()
        cancela =(input('Repetir operação, tecle [ENTER] Para finalizar, digite [000]: '))
        if(cancela == "000"):
            break
    else:
        line()
        print('\nEmpréstimo concedido')
        line()
        cancela =(input('Repetir operação, tecle [ENTER] Para finalizar, digite [000]: '))
        
        if(cancela == "000"):
            break
        

