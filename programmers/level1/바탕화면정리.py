def solution(wallpaper):
    answer = []
    
    graph = []
    
    length = len(wallpaper)
    
    for i in range(length):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j]=='#':
                graph.append((i,j))
                    
    graph.sort()
    min_y = min(graph,key = lambda x:x[1])[1]
    max_y = max(graph,key = lambda x:x[1])[1]+1
    min_x = min(graph,key = lambda x:x[0])[0]
    max_x = max(graph,key = lambda x:x[0])[0]+1
    
    answer = [min_x,min_y,max_x,max_y]

    return answer