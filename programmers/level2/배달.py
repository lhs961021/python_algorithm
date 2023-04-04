
def solution(N, road, K):
    answer = 0
    
    INF = 1e9
    
    graph = [[INF]*(N+1) for _ in range(N+1)]
    
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i==j:
                graph[i][j] = 0
    
    for i in road:
        a,b,cost = i
        graph[a][b] = min(cost,graph[a][b])
        graph[b][a] = min(cost,graph[b][a])
            
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                graph[i][j] = min(graph[i][k]+graph[k][j],graph[i][j])
    
    for i in range(1,N+1):
        if graph[1][i] <= K:
            answer += 1
    
    return answer