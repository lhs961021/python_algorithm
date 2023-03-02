def solution(board, moves):
    answer = 0
    
    length = len(board)
    
    bucket = []
    
    for i in moves:
        for j in range(length):
            if board[j][i-1] != 0:
                bucket.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(bucket)>=2:
            if bucket[len(bucket)-1]==bucket[len(bucket)-2]:
                answer += 2
                bucket.pop()
                bucket.pop()
    
    return answer