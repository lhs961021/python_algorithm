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