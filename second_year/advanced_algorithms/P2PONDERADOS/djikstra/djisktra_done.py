def start_graph() :
    
    return {
            
            #Teste 1:
             
        # 'A': {'B':1, 'C':4, 'D':200},
        # 'B': {'A':9, 'E':5},
        # 'C': {'A':4, 'F':15},
        # 'D': {'A':100, 'F':7},
        # 'E': {'B':3, 'J':7},
        # 'F': {'C':11, 'D':14, 'K':3, 'G':9},
        # 'G': {'F':12, 'I':4},
        # 'H': {'J':13},
        # 'I': {'G':6, 'J':7},
        # 'J': {'H':2, 'I':4},
        # 'K': {'F':6}

        # Teste 2:

        'A': { 'B':10, 'D':5 },
        'B': { 'C':1, 'D':2 },
        'C': { 'E':2 },
        'D': { 'B':3, 'C':9, 'E':5 },
        'E': { 'A':7, 'C':6 },
    }

print(start_graph())
    
start = input(str('Digite o vértice para Ponto de Partida: \n'))
caminho = {}
adj_vertice = {}
fila = []

graph = start_graph()

for vertice in graph:
    caminho[vertice] = float("inf")
    adj_vertice[vertice] = None
    fila.append(vertice)
    
caminho[start] = 0

while fila:
    key_min = fila[0]
    min_val = caminho[key_min]
    for n in range(1, len(fila)):
        if caminho[fila[n]] < min_val:
            key_min = fila[n]  
            min_val = caminho[key_min]
    cur = key_min
    fila.remove(cur)
    print(cur)
    
    for i in graph[cur]:
        alternate = graph[cur][i] + caminho[cur]
        if caminho[i] > alternate:
            caminho[i] = alternate
            adj_vertice[i] = cur


destino = input(str('Digite a Letra do vértice de Destino:'))

print(f'O caminho caminho entre o ponto de partida [ {start} ] e o Destino [ {destino} ]')

print(destino, end = ' <- ')
while True:
    destino = adj_vertice[destino]
    if destino is None:
        print("")
        break
    print(destino, end='')