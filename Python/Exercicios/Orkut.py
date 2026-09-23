# Exercicio do Neps Academy

from collections import deque

amigo, quantAmg = map(int, input().split())
# quantAmg --> Quantidade de amigos que ela precisa ser amigo antes

grafo = [[] for i in range(amigo + 1)]

for i in range(quantAmg):
    u, v = map(int, input().split())
    grafo[u].append[v]
    grafo[v].append[u]

dist = [-1] * (amigo + 1)

fila = deque([0])
dist[0] = 0

while fila: 
    u = fila.popleft()

    for v in grafo[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            fila.append(v)

# INCOMPLETO

# print(f"Teste {teste}")
# print(f"aaa")
# print("")