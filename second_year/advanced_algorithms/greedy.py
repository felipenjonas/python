def troco(n, moedas):
    # Insere no vetor A as quantidades de cada moeda;
    A = []

    for i in range(len(moedas)):
        num_moedas = n//moedas[i]
        n -= num_moedas * moedas[i]
        # Gerar o vetor A
        A.append(num_moedas)

    return A


moedas = [100, 25, 10, 5, 1]
S = []

val = float(input("Digite o valor do troco em R$: "))
val_int = int(val*100)

S = troco(val_int, moedas)
# print em S juntamente com moedas e calcular o total de moedas
total = 0
for i in range(len(S)):
    if (S[i] > 0):
        print(S[i], "moedas de ", moedas[i])
        total += S[i]
print("Total de moedas = ", total)
