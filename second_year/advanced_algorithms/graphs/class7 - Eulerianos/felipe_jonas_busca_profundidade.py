grafo = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C']}

def busca_profundidade(grafo, inicio):
    destino = []
    pilha = []
    visitados = []
    
    pilha.append(inicio)
    visitados.append(inicio)

    while pilha:
        vertice = pilha.pop()
        destino.append(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                visitados.append(vizinho)
                pilha.append(vizinho)
    print(destino)


vertice_inicial = input("Digite o vértice inicial da busca em profundidade: ")

busca_profundidade(grafo, vertice_inicial)