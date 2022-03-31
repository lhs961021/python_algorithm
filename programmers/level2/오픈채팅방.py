def solution(record):
    user = dict()
    graph = []
    answer = []

    for i in record:
        a = i.split()

        action,id = a[0],a[1]

        if action=="Enter" or action=="Change":
            user[id]=a[2]

        graph.append((action,id))

    for j in graph:
        action,id = j[0],j[1]
        if action=="Enter":
            answer.append(f'{user[id]}님이 들어왔습니다.')
        elif action=="Leave":
            answer.append(f'{user[id]}님이 나갔습니다.')

    return answer