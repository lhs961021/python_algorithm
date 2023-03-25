from itertools import combinations
from collections import Counter

def solution(orders, course):
        
    answer = []

    for i in course:
        z = []
        for j in orders:
            for k in combinations(j, i):
                z.append(''.join(sorted(k)))

        a = Counter(z).most_common()

        max = 0

        for m in a:
            if m[1]>=max:
                max = m[1]

        for l in a:
            if l[1]==max and l[1]!=1:
                answer.append(l[0])
    answer.sort()
    
    return answer

from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for i in course:
        l = []
        for order in orders:
            order = list(order)
            order.sort()
            l.extend(list(combinations(order,i)))

        for idx,i in enumerate(sorted(Counter(l).items(),key = lambda x : -x[1])):

            if idx == 0:
                flag = i[1]
                if flag == 1:
                    break
                answer.append("".join(i[0]))
            else:
                if i[1] == flag:
                    answer.append("".join(i[0]))
                else:
                    break
    
    answer.sort()
    
    return answer