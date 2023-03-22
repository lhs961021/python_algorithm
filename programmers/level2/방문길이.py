def solution(dirs):
    answer = 0
    
    dic = {}
    
    for i in range(-5,6):
        for j in range(-5,6):
            dic[(i,j)] = []

    start_x = 0
    start_y = 0

    for i in dirs:
        if i == "U":
            if start_y+1 <= 5:
                end_x = start_x
                end_y = start_y+1
            else:
                continue
        elif i == "D":
            if start_y-1 >= -5:
                end_x = start_x
                end_y = start_y-1
            else:
                continue
        elif i == "L":
            if start_x-1 >= -5:
                end_x = start_x-1
                end_y = start_y
            else:
                continue
        else:
            if start_x+1 <= 5:
                end_x = start_x+1
                end_y = start_y
            else:
                continue
                
        if (end_x,end_y) not in dic[(start_x,start_y)] and (start_x,start_y) not in dic[(end_x,end_y)]:
            dic[(start_x,start_y)].append((end_x,end_y))
            dic[(end_x,end_y)].append((start_x,start_y))
            answer += 1
        
        start_x,start_y = end_x,end_y
            
    return answer