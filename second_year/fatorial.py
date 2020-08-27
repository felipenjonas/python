number = int(input('Digite um numero: \n'))

if (number<0):
    print('Não existe fatorial de números negativos ou em zero')

else:
    fat = 1
    for i in range(number ,1 ,-1):
        fat*= i

    print(f'fatorial de {number} é: \n ')
    print(f'{fat}')