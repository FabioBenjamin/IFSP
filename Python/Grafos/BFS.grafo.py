# Exercicio feito pelo geekdforgeeks.com 
# Nivel de dificuldade: Fácil

from collections import deque

class Solution:
    def bfs(self, adj):
        queue = [0]
        solution = set()
        arm = []
        
        while(queue):
            atual = queue[0]
            arm.append(atual)
            solution.add(atual)
            queue.pop(0)
            
            if(True):
                for i in adj[atual]:
                    if not i in solution:
                        queue.append(i)
                        solution.add(i)
                
        return arm