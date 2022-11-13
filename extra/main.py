import math


def Convertb10(string):
    listb10 = []
    listb10[:0] = string
    exp = len(listb10)
    base_list = []
    total = 0

    for x in listb10:
        exp -= 1
        value = (int(x)*2)**exp
        base_list.append(value)

    for x in base_list:
        total += x

    print(f'O número {num} na base 2 transformado para base 10 é: {total}')


def Convertb2(int):
    num = int
    list_resto = []
    list_div = []

    while (True):
        value = num / 2
        # Converter valor da divisão para inteiro
        floor_value_num = math.floor(value)
        # Inserir na lista o valor da divisão(Array)
        list_div.append(floor_value_num)
        # Calcula o resto
        resto = num % 2
        # Converter o resto para inteiro usando método "floor" da lib importada "math"
        math.floor(resto)
        # Inserir na lista o resto da divisão(Array)
        list_resto.append(resto)
        # Atualiza o valor de num para a próxima sequência
        num = floor_value_num

        # Condicional para parar as divisões.
        if num < 1:
            break
        else:
            continue

    # Alterar a ordem do nosso array de resto
    list_resto.reverse()
    string_final = ""

    for x in list_resto:
        string_final += str(x)

    # print(list_resto)
    print(
        f'O número {num2} na base 10 transformado para base 2 é: {string_final}')


def Erro_absoluto(float1, float2):
    exato = float1
    aprox = float2

    result = exato - aprox
    result = abs(result)
    print(f'O valor de Erro Absoluto é: {result:.4f}')


def Erro_relativo(float1, float2):
    exato = float1
    aprox = float2

    result = exato - aprox
    result = abs(result)

    value_erro_relativo = result / exato
    convert_to_percent = value_erro_relativo * 100
    print(f'O valor de Erro relativo é: {convert_to_percent:.3f}%')


while (True):
    print("-"*30)
    print("MENU - MÉTODOS NUMÉRICOS \n")

    print("Digite [1] para escolher Erro Relativo: \n")
    print("Digite [2] para escolher Absoluto: \n")
    print("Digite [3] para converter base 2 para 10: \n")
    print("Digite [4] para converter base 10 para 2 \n")
    print("Digite [0] para sair do programa \n")
    print("-"*30)
    opt = str(input("Digite apenas o número: "))

    if (opt == "1"):
        x = float(input("\nDigite o valor exato: "))
        x_line = float(input("\nDigite o valor aproximado: "))
        Erro_relativo(x, x_line)
        continue
    elif (opt == "2"):
        x = float(input("\nDigite o valor exato: "))
        x_line = float(input("\nDigite o valor aproximado: "))
        Erro_absoluto(x, x_line)
        continue
    elif (opt == "3"):
        num = str(input("Digite o número binário: \n"))
        Convertb10(num)
        continue
    elif (opt == "4"):
        num2 = int(input("Digite o número de base 10: \n"))
        Convertb2(num2)
        continue
    elif (opt == "0"):
        break
