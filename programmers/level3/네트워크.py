from collections import deque

def solution(n, computers):
    
    visited = [0]*(n)
    answer = 0
    
    def bfs(start,visited):
        queue = deque([start])

        while queue:
            a = queue.popleft()
            visited[a] = 1
            counter = 0

            for i in computers[a]:
                if visited[counter]==0 and i==1:
                    queue.append(counter)
                counter += 1


    for i in range(n):
        if visited[i]==0:
            bfs(i,visited)
            answer += 1
    
    
    
    return answer

from collections import deque

def solution(n, computers):
    answer = 0
    
    def bfs(start):
        visited = [0]*(n)
        queue = deque()
        queue.append(start)
        
        while queue:
            a = queue.popleft()
            if visited[a] == 0:
                visited[a] = 1
                for i in range(n):
                    if computers[a][i] == 1:
                        queue.append(i)
                        
        return visited
    
    real_visited = [0]*(n)
    
    for i in range(n):
        if real_visited[i] != 1:
            v = bfs(i)
            for j in range(len(v)):
                if v[j]==1:
                    real_visited[j] = 1
            answer += 1
    
    return answer