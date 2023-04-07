from collections import deque

def solution(maps):
    answer = []
    
    length_x = len(maps)
    length_y = len(maps[0])
    
    graph = [list(i) for i in maps]
    visited = [[0]*length_y for _ in range(length_x)]
    
    def bfs(x,y,visited,graph):
        
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        
        queue = deque()
        queue.append((x,y))
        result = 0
        
        while queue:
            x,y = queue.pop()
            result += int(graph[x][y])
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if nx<0 or ny<0 or nx>=length_x or ny>=length_y:
                    continue
    
                if visited[nx][ny] == 0 and graph[nx][ny]!='X':
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                
        return result
    
    for i in range(length_x):
        for j in range(length_y):
            if visited[i][j]==0:
                visited[i][j] = 1
                if graph[i][j] != 'X':
                    answer.append(bfs(i,j,visited,graph))  
    
    if len(answer) == 0:
        return [-1]
    
    
    answer.sort()
    
    
    
    return answer