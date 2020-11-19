from tabulate import tabulate


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

def line():
    print('\n')
    print('-'*60)


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

# Criar outra Lista com tabela


# Criar a ordenação do Grafo pelo PESO:
def ordenaGrafo():
    line()

    tab = []
    i = 0


    for v in grafo.keys():
        
        for a in grafo[v]:
            aresta = [v]
            aresta.insert(1,a[0])
            aresta.insert(2,a[1])
            tab.insert(i,aresta)
            i += 1

     
    # Ordenando a tabela - algoritmo de "bubble sort"
    for j in range(i):
        for k in range(j,i):
            if tab[j][2] > tab[k][2]:
                tab[j][2], tab[k][2] = tab[k][2], tab[j][2]

    for j in range(i):
        print(tab[j])


# Montar a AGM, pela ordem criada, Insere uma e pergunta, se terminou, depois quando inserir todos os vértices
#  No final verifica se esta tudo conectado, se sim, acabou.
# custo da agm é somar as arestas, essa agm foi geradda com custo 12












    # print(tabulate(
    #     [
    #         # ['0 - '+ grafo['0'][0][0], grafo['0'][0][1]],
            
            
            
    #     ], 
    #     headers=['Aresta','Peso']
    # ))



# print_vertices()
# line()
# print_arestas()

ordenaGrafo()





