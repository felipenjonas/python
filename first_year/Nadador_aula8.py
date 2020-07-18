# 1) Elabore um programa em python que dada a idade
# de um nadador classifique-o em uma das categorias:
# - Infantil A = 5 a 7 anos;
# - Infantil B = 8 a 11 anos;
# - Juvenil A = 12 a 13 anos;
# - Juvenil B = 14 a 17 anos;
# - Adultos = maiores de 18 anos.


while(True):
    idade = (int(input('\nDigite sua idade nadador: ')))
    if(idade >= 5 and idade <=7): 
        print('\nCategoria: Infantil A')
    if(idade >= 8 and idade <=11): 
        print('\nCategoria: Infantil B')
    if(idade >= 12 and idade <=13): 
        print('\nCategoria: Juvenil A')
    if(idade >= 14 and idade <=17): 
        print('\nCategoria: Juvenil B')
    if(idade >= 18): 
        print('\nCategoria: Adulto')
    if(idade <=4):
        print('\nSem categoria')
    
