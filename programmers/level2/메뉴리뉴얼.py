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