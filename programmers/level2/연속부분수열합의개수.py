from itertools import combinations

def solution(elements):
    answer = set()
    
    for i in elements:
        answer.add(i)

    length = len(elements)
    elements = elements*2
    
    for i in range(2,length+1):
        for j in range(len(elements)-i+1):
            answer.add(sum(elements[j:j+i]))

    return len(answer)