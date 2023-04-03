# def solution(board):
#     answer = 0

#     length_x = len(board)
#     length_y = len(board[0])
#     l = min(length_x,length_y)
    
#     if length_x==1:
#         for i in board[0]:
#             if i==1:
#                 return 1
#         return 0
    
#     if length_y==1:
#         for i in board:
#             if i[0]==1:
#                 return 1
#         return 0
                
#     def check(start_x,start_y,n):
#         if start_x+n>length_x or start_y+n>length_y:
#             return False
        
#         for i in range(start_x,start_x+n):
#             for j in range(start_y,start_y+n):
#                 if board[i][j]!=1:
#                     return False
#         return n**2
    
#     for k in range(1,l+1):
#         for i in range(length_x):
#             for j in range(length_y):
#                 if check(i,j,k)!=False:
#                     answer = check(i,j,k)
                
#                 if answer == (l**2):
#                     return answer
                
#     return answer

def solution(board):
    answer = 0

    length_x = len(board)
    length_y = len(board[0])

    for i in range(1,length_x):
        for j in range(1,length_y):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1],board[i][j-1],board[i-1][j])+1
    
    for i in board:
        answer = max(max(i),answer)
            
    return answer ** 2