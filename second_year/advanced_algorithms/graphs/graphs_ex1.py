def insere_aresta(g, a, b):
    if a not in g:
        g[a]=[ ]
    if b not in g:
        g[b]=[ ]
    g[a].append(b)
    g[b].append(a)

def imprime_grafo(g):
    for v,a in g.items():
        print("="*50)
        print('Vertice:', v)
        print('Adjacentes:', a)

def verifica_aresta(g,a,b):
    if b in g[a]:
        return True
    else:
        return False


def adjacentes(g,x):
    return g[x]
# Método que dado um grafo e um vértice, retorne com o seu grau (numero inteiro das arestas incidentes)



def regular(g):
    g1 = grau(g.keys()[0])
    for v in g.keys():
        g2 = grau(g[v])
        if g1 != g2:
            return False
    return True 


# ============================================================================

grafo = { }
while True:
    x = input("Entre com o vértice ou FIM para encerrar: ")
    if x=='FIM':
        break
    y = input("Entre com um vertice adjacente:")

    insere_aresta(grafo, x, y)


imprime_grafo(grafo)
# ============================================================================


x = input('Digite o vértice que deseja saber os adjacentes:')
if x in grafo:
    print('Grau do vertice', x, ' = ', grau(grafo[x]))
else:
    print('Não existe este vértice!')

# ============================================================================


x = input('Digite o vértice que deseja saber o grau:')
if x in grafo:
    print('Grau do vertice', x, ' = ', adjacentes(grafo, x))
else:
    print('Não existe este vértice!')

# ============================================================================
# EX = D)

x = input('Digite o primeiro vertice a verificar a existência de aresta: ')
y = input('Digite o sedundo vertice a verificar existencia de arestas:')
if (x in grafo and y in grafo):
    if (verifica_aresta(grafo,x,y)):
        print(f'Existe aresta entre os vertices: {x} e {y} ')
    else:
        print(f'Não existe aresta entre os vertices: {x} e {y} ')
else:
    print('Algum destes vertices não existe no grafo!')

# A fazer
# ============================================================================
# EX F) Veriicar se o grafo é regular: Um grafo é regular se todos os vértices ,possuem mesmo grau
# 
# 
# 
# ============================================================================
# Ex G) Verificar se o grafo é completo. Um grafo ,completo de N vértices, o grau de cada vértice é N-1
# 
# 
# 
# ============================================================================











