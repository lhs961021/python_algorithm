# 1. 레버까지 최단 길찾기를 돌리고
# 2. 레버부터 도착지까지 최단 길찾기를 돌린다
from collections import deque

def solution(maps):
    answer = 0

    length_x = len(maps)
    length_y = len(maps[0])
    
    for i in range(length_x):
        for j in range(length_y):
            if maps[i][j]=='L':
                lever_x,lever_y = i,j
            elif maps[i][j]=='S':
                start_x,start_y = i,j

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    def bfs(x,y,end,cnt):
        queue = deque()
        queue.append((x,y,cnt))
        visited = [[0]*length_y for _ in range(length_x)]
        
        while queue:
            x,y,cnt = queue.popleft()
            
            if maps[x][y] == end:
                return cnt
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx<0 or ny<0 or nx>=length_x or ny>=length_y:
                    continue
                
                if maps[nx][ny]!='X' and visited[nx][ny]==0:
                    queue.append((nx,ny,cnt+1))
                    visited[nx][ny] = 1
            
        return -1

    a = bfs(start_x,start_y,'L',0)
    b = bfs(lever_x,lever_y,'E',0)

    if a == -1 or b == -1:
        return -1
    else:
        return a+b
    