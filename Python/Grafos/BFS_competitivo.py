from collections import deque

n, m = map(int(input().split()))

# Cria o grafo
grafo = [[] for i in range(n + 1)]

for i in range(m):
    # U --> Origem (Vertice atual) ; V --> Destino (Outro vertice)
    u, v = map(int, input().split())
    grafo[u].append(v)
    grafo[v].append(u)

# Começa no -1 porque não descobriu o vértice
dist = [-1] * (n + 1)

# Começa o BFS 
fila = deque([1]) # Começa a busca no indice 1 
dist[1] = 0 # Muda esse indice de 1 para 0

# Enquanto haver elementos na fila roda esse loop
while fila: 
    u = fila.popleft() # Primeiro elemento da fila

    for v in grafo[u]:
        if dist[v] == -1: # Verifica se foi não foi visitado ainda 
            dist[v] = dist[u] + 1 # Caso ainda não foi visitado vai pro outro
            fila.append(v)

print(dist)