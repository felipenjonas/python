# A cada inserção de arestas, chama o método para saber se é AGM. Se verdadeiro então termina.


def verifica_agm(grafo, v):
    pilha = []
    visitados = []
    pilha.append(v)
    topo = 0 
    visitados.append(v)

    # Enquanto a pilha não estiver vazia
    while (len(pilha)> 0):
        n = pilha[topo]
        pilha.pop()
        topo -= 1

        for item in grafo[n]:
            visitado.append(item[0])
            pilha.append(n)
            topo += 1
            pilha.append(item[0])
            topo+=1





