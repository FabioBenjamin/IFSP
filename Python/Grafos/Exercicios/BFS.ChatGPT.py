# Exercicio feito pelo ChatGPT de nível fácil sobre BFS

from collections import deque 

pessoas, amizades = map(int, input().split())

grafo = [[] for i in range(pessoas + 1)]

for i  in range(amizades):
    u, v = map(int, input().split())
    grafo[u].append(v)
    grafo[v].append(u)

dist = [-1] * (pessoas + 1)

fila = deque([0])
dist[0] = 0

while fila:
    u = fila.popleft()

    for v in grafo[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            fila.append(v)

print(dist)