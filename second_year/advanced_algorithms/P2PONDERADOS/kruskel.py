# EXEMPLO DE CRIAR O GRAFO PONDERADO com algoritmo de Kruskel
grafo = { 
    '0': [
        ['1', 6],
        ['2', 1],
        ['3', 5]
    ],
    '1': [
        ['0', 6],
        ['2', 2],
        ['4', 5]
    ],
    '2': [
        ['0', 1],
        ['1', 2],
        ['3', 2],
        ['4', 6],
        ['5', 4]
    ],
    '3': [
        ['0', 5],
        ['2', 2],
        ['5', 4]
    ],
    '4': [
        ['1', 5],
        ['2', 6],
        ['5', 3],
    ],
    '5': [
        ['2', 4],
        ['3', 4],
        ['4', 3]
    ]
}

# Consultar os vértices do Grafo:
def print_vertices():
    for vertice in grafo:
        vertices = [vertice[0:5]]
        print(vertices)

# Consultar as arestas ponderadas de cada vértice do Grafo:
def print_arestas():
    for aresta in grafo.values():
        print(f'\n{aresta}')

def valida_ciclo():
    print()

# Criar a ordenação do Grafo:
def ordenaGrafo():
    


print_vertices()
print_arestas()















