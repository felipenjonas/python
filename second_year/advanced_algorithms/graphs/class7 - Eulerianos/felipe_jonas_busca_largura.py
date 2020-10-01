grafo = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C']}
         
         
def bfs(grafo, inicial):
    
    visitado = []
    
    fila = [inicial]
 
    while fila:
        
        node = fila.pop(0)
        if node not in visitado:
            
            visitado.append(node)
            adjacentes = grafo[node]
 
            
            for vizinho in adjacentes:
                fila.append(vizinho)
    return visitado
 
print(bfs(grafo,'A'))