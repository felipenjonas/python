# Felipe Gabriel Novais Jonas
# Trabalho P2 - AGM | Kruskal 


def verifica_agm(G,v):
    pilha = []
    visitados = []
    pilha.append(v)
    topo=0

    visitados.append(v)
    # enquanto a pilha nao estiver vazia
    while (len(pilha)>0):
        n = pilha[topo]
        pilha.pop()
        topo-=1
        for item in G[n]:
            if item[0] not in visitados:
                visitados.append(item[0])
                pilha.append(n)
                topo+=1
                pilha.append(item[0])
                topo+=1
                n = item[0]

    if (len(visitados) == len(G.keys())):
        return True
    else:
        return False
# aresta = ['A',['B',2]]

def gerar_tab(G, tab):
    for x,y in G.items():
        for a in y:
            aresta = []
            aresta.append(x)
            aresta.append(a)

            tab.append(aresta)

def ordenar(tab):
    for i in range (len(tab)):
        for j in range (i+1, len(tab)):
            if (tab[i][1][1]>tab[j][1][1]):
                tab[i],tab[j] = tab[j],tab[i]

def gerar_agm(agm, tot_vert , tab):
    #  Vamos usar uma variável "I" para nos ajudar a indicar qual linha em tab() que será inserida na AGM
    i = 0
    # soma = o custo = total de arestas inseridas
    soma = 0

    # Enquanto a AGM não estiver finalizada, inserir a próxima aresta de tab()
    #  Criar a AGM do mesmo modo como foi criado o dicionário de grafo.

    # Inserindo tanto as arestas de "ida" quanto as de "volta"
    while (True):
        if (tab[i][0] not in agm):
            agm[tab[i][0]] = []

        if (tab[i][1][0] not in agm):
            agm[tab[i][1][0]] = []

        #  Inserindo as arestas
        if (tab[i][1] not in agm[tab[i][0]]):
            agm[tab[i][0]].append(tab[i][1])
            soma += tab[i][1][1]
        adj = [tab[i][0], tab[i][1][1]]
        if adj not in agm [tab[i][1][0]]:
            agm [tab[i][1][0]].append(adj)
            soma += adj[1]

        #  AGM tá pronta?

        if (len(agm.keys())==tot_vert) and verifica_agm(agm, tab[0][0]):
            break

        i += 1

    return soma/2

# ====================  programa principal =================================

grafo={
    'A':
        [
            ['B',6],
            ['C',1],
            ['D',5]
        ],
    'B':
        [
            ['A',6],
            ['C',2],
            ['E',5]
        ],
    'C':
        [
            ['A',1],
            ['B',2],
            ['D',2],
            ['E',6],
            ['F',4]
        ],
    'D':
        [
            ['A',5],
            ['C',2],
            ['F',4]
        ],
    'E':
        [
            ['B',5],
            ['C',6],
            ['F',3]
        ],
    'F':
        [
            ['C',4],
            ['D',4],
            ['E',3]
        ]
}


# tab é a tabela com as arestas... deverá ser ordenada.
tab = []
agm = { }

print("\nGrafo:")
for v,a in  grafo.items():
    print(v,a)

gerar_tab(grafo, tab)

ordenar (tab)


if verifica_agm(grafo, tab[0][0]):
    custo = gerar_agm(agm, len(grafo.keys()), tab)

    print("\nAGM:")
    for v,a in  agm.items():
        print(v,a)
        
    print("\nCusto = ", int(custo))
else:
    print("\nOpsss..Grafo desconexo! Não existe AGM")
