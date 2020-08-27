# calcular a dezena de um número:

def Exemplo1():
    print((int(input('digite um número')) // 10) % 10)

def Exemplo2():
    a = input("insira um numero: ")
    dezena = a.split()
    dezena = a[-2]

    print(f'A dezena do número {a} é: {dezena}')

Exemplo2()

Exemplo2() 