# <====> Exercício 1 <====>
# Elabore um programa que implemente funções para:
#   |(a) Permita o armazenamento de um grafo com "n" vértices em forma de matriz de adjacências;
#   |(b) Visualizar os grafos (todas as arestas);
#   |(c) Visualizador os vértices adjacentes de um determinado vértice;
#   |(d) Dados 2 vértices (v1 e v2) verificar a existência de uma aresta entre eles;
#   |(e) Calcular o grau de um vértice específico;

def matriz_Adjacente(n):
    n = int (input("Digite o total de vertices: "))
    a = [0]*n


    for i in range(n):
        a[i] = [0]*n
        
        for j in range(n):
            a[i][j] = 1

    for j in a:
        print(j)

matriz_Adjacente(6)