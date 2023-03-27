def solution(m, n, board):
    
    for i in range(m):
        board[i] = list(board[i])
    
    global check_list
    check_list = []
    
    answer = 0
    
    def check(x,y,board):
        
        flag = board[x][y]
        if flag == '0':
            return
        
        l = [(x,y)]
        dx = [0,1,1]
        dy = [1,0,1]
        
        for i in range(3):
            nx = dx[i] + x
            ny = dy[i] + y
            if board[nx][ny]!=flag:
                return
                
            l.append((nx,ny))
        
        check_list.extend(l)
        
        return
        
    while 1:
        for i in range(m-1):
            for j in range(n-1):
                check(i,j,board)
        
        if len(check_list)==0:
            break
        
        check_list = list(set(check_list))
        answer += len(check_list)
        
        for i in check_list:
            board[i[0]][i[1]] = '0'
        
        for i in range(m-1,1,-1):
            for j in range(n):
                if board[i][j]=='0':
                    for x in range(i-1,-1,-1):
                        if board[x][j] != '0':
                            board[i][j],board[x][j] = board[x][j],board[i][j]
                            break
        
        check_list = []
                
    return answer