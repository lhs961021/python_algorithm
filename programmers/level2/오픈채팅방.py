from collections import deque

def solution(record):
    answer = []
    
    queue = deque()
    dic = {}
    
    for i in record:
        a = i.split(' ')
        if a[0]=="Leave":
            queue.append((a[1],a[0]))
        elif a[0] == 'Enter':
            dic[a[1]] = a[2]
            queue.append((a[1],a[0]))
        else:
            dic[a[1]] = a[2]
    
    while queue:
        user, work = queue.popleft()
        if work == "Enter":
            answer.append("{0}님이 들어왔습니다.".format(dic[user]))
        else:
            answer.append("{0}님이 나갔습니다.".format(dic[user]))


    return answer