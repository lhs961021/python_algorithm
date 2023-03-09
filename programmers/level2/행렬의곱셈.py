import numpy

def solution(arr1, arr2):
    answer = []
    
    A = numpy.array(arr1)
    B = numpy.array(arr2)
    
    a = numpy.dot(A,B)
    l = list(a)
    
    for i in l:
        k = []
        for j in list(i):
            k.append(int(j))
        answer.append(k)
    
    return answer