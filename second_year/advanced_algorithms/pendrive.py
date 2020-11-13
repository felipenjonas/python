def preenche(P, arquivos, cap):
    soma = 0
    # 'I' irá marcar  arquivo que irá para o pendrive
    i = 0

    while(soma < cap and i < len(arquivos)):
        soma += arquivos[i][1]
        P.append(arquivos[i])
        i += 1

    if (soma > cap):
        soma -= arquivos[i-1][1]
        P.pop()

    return soma


cap = int(input('Digite a capacidade do pendrive: '))

arquivos = [
    ['A',5],
    ['B',10],
    ['C',10],
    ['D',15],
    ['E',20],
    ['F',20],
    ['G',30],
    ['H',40],
    ['I',50]
    
]

# Caso os tamanhos dos arquivos fossem lidos pelo teclado, seria necessário ordená-los
# Total é igual a quantidade ocupado pelo pendrive

P = []

total = preenche(P, arquivos, cap)

print('Arquivos no pendrive:')
print(P)
print('Capacidade usada no pendrive: ', total)

