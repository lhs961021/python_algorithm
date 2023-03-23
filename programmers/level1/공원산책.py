from collections import deque

def solution(park, routes):
    answer = []
    
    x = len(park)
    y = len(park[0])
    
    new_park = []
    
    for i in range(x):
        new_park.append(list(park[i]))
        if "S" in park[i]:
            start_x, start_y = i,park[i].index("S")
    
    for i in routes:
        where, how = i.split(' ')
        flag = 0
        
        if where == "E":
            if 0<=start_y+int(how)<y:
                for i in range(start_y,start_y+int(how)+1):
                    if new_park[start_x][i]=='X':
                        flag = 1
                        break
                if flag == 0:
                    start_y = start_y+int(how)
            
        elif where == "W":
            if 0<=start_y-int(how)<y:
                for i in range(start_y-int(how),start_y+1):
                    if new_park[start_x][i]=='X':
                        flag = 1
                        break
                if flag == 0:
                    start_y = start_y-int(how)
        
        elif where == "S":
            if 0<=start_x+int(how)<x:
                for i in range(start_x,start_x+int(how)+1):
                    if new_park[i][start_y]=='X':
                        flag = 1
                        break
                if flag == 0:
                    start_x = start_x+int(how)
            
        else:
            if 0<=start_x-int(how)<x:
                for i in range(start_x-int(how),start_x+1):
                    if new_park[i][start_y]=='X':
                        flag = 1
                        break
                if flag == 0:
                    start_x = start_x-int(how)
                
    return [start_x,start_y]
    