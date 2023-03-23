def solution(arr):
    answer = [0,0]
    length = len(arr)
    
    def check(x,y,length):
        first = arr[x][y]
        for i in range(x,x+length):
            for j in range(y,y+length):
                if arr[i][j]!=first:
                    length = length//2
                    check(x,y,length)
                    check(x,y+length,length)
                    check(x+length,y,length)
                    check(x+length,y+length,length)
                    return
        
        answer[first] += 1 
    
    check(0,0,length)
    
    return answer