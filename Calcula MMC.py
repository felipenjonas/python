# # 3) Faça um programa em python que leia 2 números e
# # que calcule o mínimo múltiplo comum usando while e
# # if.

def line_():
    print('-'*30)


num1 = int(input("\nDigite um número inteiro:"))
num2 = int(input("\nDigite outro número inteiro:"))

if(num1 > num2):
    maior = num1
else:
    maior = num2

while (True):  
   

    if maior % num1 == 0 and maior % num2 == 0:
        line_()
        print(maior)
        break
    else:
        maior +=1
