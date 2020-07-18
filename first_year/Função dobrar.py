# Definir uma função que dobro o valor digitado pelo usuário

# def dobrar():
#     num1 = int(input('\nDigite um número:'))
#     print ('O dobro de {} é: {}'.format(num1,num1*2))

# dobrar()

# def dobra(num1):
#     print(f'{dobrar=num1*2}')
#     return

# num1 = input('Digite um número: ')

# dobra()


# Jeito correto de fazer função com entradas e saídas
def dobro(num):
    return num *2

numero = int(input('\nDigite um número: '))
resultado = dobro(numero)
print(f'\nO dobro de {numero} é: {resultado}')