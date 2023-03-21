from collections import deque

def solution(maps):
    answer = 0
    
    

    def bfs(x,y,maps):
        
        x_length = len(maps)
        y_length = len(maps[0])
        
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        
        queue = deque()
        queue.append((x,y))
        
        while queue:
            x,y = queue.popleft()
            
            for i in range(4):
                nx = dx[i]+x
                ny = dy[i]+y
                
                if nx<0 or nx>=x_length or ny<0 or ny>=y_length:
                    continue
                
                if maps[nx][ny]==0:
                    continue
                
                if maps[nx][ny]==1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
                                        
        if maps[x_length-1][y_length-1] == 0 or maps[x_length-1][y_length-1] == 1:
            return -1
        else:
            return maps[x_length-1][y_length-1]
    
    answer = bfs(0,0,maps)
    
    return answer