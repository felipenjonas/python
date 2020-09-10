# ==|AULA-07|==||||== DATA: 10/09/2020|==
# (a) Entrar com 2 vértices e verificar se há caminho entre eles.
# (b) Entrar com o primeiro vértice, e verificar se  há ciclo iniciado e terminado  neste vértice.
# (c) Verificar  se o grafo é Euleriano (Analisar o grau de cada vértice). 

def insere_aresta(g, a, b):
    if a not in g:
        g[a]=[]
    if b not in g:
        g[b]=[]
    g[a].append(b)
    g[b].append(a)

def imprime_grafo(g):
    for v,a in g.items():
        print("="*50)
        print('Vertice:', v)
        print('Adjacentes:', a)

# Método que dado um grafo e um vértice, retorne com o seu grau (numero inteiro das arestas incidentes)


grafo = { }
while True:
    x = input("Entre com o vértice ou FIM para encerrar: ")
    if x=='FIM':
        break
    y = input("Entre com um vertice adjacente:")

    insere_aresta(grafo, x, y)

imprime_grafo(grafo)





