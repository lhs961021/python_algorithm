def solution(places):
    answer = []
    
    def check(graph):
        dx = [0,0,1,-1,0,0,2,-2,1,-1,1,-1]
        dy = [-1,1,0,0,-2,2,0,0,1,1,-1,-1]
        
        for i in range(5):
            for j in range(5):
                if graph[i][j]=='P':
                    flag = [0,0,0,0]
                    for k in range(12):
                        nx = dx[k]+i
                        ny = dy[k]+j
                        
                        if 0<=nx<5 and 0<=ny<5:
                        
                            if graph[nx][ny]=='P':
                                if 0<=k<=3:
                                    return False
                                elif 4<=k<=7:
                                    if flag[k-4] == 1:
                                        return False
                                else:
                                    if k==8:
                                        if flag[2]==1 or flag[1]==1:
                                            return False
                                    elif k==9:
                                        if flag[3]==1 or flag[1]==1:
                                            return False
                                    elif k==10:
                                        if flag[0]==1 or flag[2]==1:
                                            return False
                                    else: 
                                        if flag[0]==1 or flag[3]==1:
                                            return False
                            else:
                                if 0<=k<=3:
                                    if graph[nx][ny]=='O':
                                        flag[k] = 1
    
        return True
    
    for i in places:
        graph = []
        for j in i:
            graph.append(list(j))
        
        if check(graph)==True:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer