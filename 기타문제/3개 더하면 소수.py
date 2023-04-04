from itertools import combinations

def solution(nums):

    def check(num):

        for i in range(2,int(num**(1/2))+1):
            if num%i==0:
                return False
        
        return True
    
    answer = 0

    for i in list(combinations(nums,3)):
        if check(sum(i)):
            answer += 1

    return answer