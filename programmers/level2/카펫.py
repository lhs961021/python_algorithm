def solution(brown, yellow):

    l = []
    
    for i in range(1,int(yellow**(1/2))+1):
        if yellow % i == 0:
            l.append(i)
            
    for i in l:
        if brown == ((2*(i+2))+(2*(yellow//i))):
            return [(yellow//i)+2,i+2]