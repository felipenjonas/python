def armazena_vertice_em_lista():
    
    seq = 1
    for v in range (total_vertices):
        v = input(f'Digite o {seq}° vértice: \n')
        lista_de_vertices.append(v)
        seq += 1

def armazena_arestas():
    posicao = 0

    for aresta in range(len(lista_de_vertices)):
        vertice = lista_de_vertices[posicao]

        grau = int(input(f'Qual o grau do vértice {vertice}: \n'))

        for aresta in range(grau):
            aresta = input(f'Digite uma aresta conectada ao vértice {vertice}: \n')
            arestas = []
            arestas.append(aresta)
            item = lista_de_arestas.append(arestas)
        
        posicao += 1
        


lista_de_vertices = [ ]
lista_de_arestas = [ ]

total_vertices = int(input('Digite o total de vértices que deseja incluir: '))




armazena_vertice_em_lista()

armazena_arestas()

print(lista_de_vertices)
print(lista_de_arestas)