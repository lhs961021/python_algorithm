from collections import deque
from copy import deepcopy

def solution(n, wires):
    answer = 10000000
    
    graph = [[] for _ in range(n+1)]
    
    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    def bfs(graph,s,value,start):
        graph[s].remove(value)     
        graph[value].remove(s)
        
        queue = deque()
        queue.append(start)
        
        visited = [0]*(n+1)
        
        while queue:
            v = queue.popleft()
            visited[v] = 1
            
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
        
        return abs((sum(visited)*2)-n)

    for i in range(1,n+1):
        for j in range(len(graph[i])):
            check = deepcopy(graph)
            a = check[i][j]
            answer = min(bfs(check,i,a,1),answer)
            
    
    return answer