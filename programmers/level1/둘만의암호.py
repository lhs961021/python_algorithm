def solution(s, skip, index):
    answer = ''
    
    dic = ['a','b','c','d','e','f','g',
           'h','i','j','k','l','m','n',
           'o','p','q','r','s','t','u',
           'v','w','x','y','z'
          ]
    
    for i in skip:
        dic.remove(i)
        
    for j in s:
        x = dic.index(j)
        a = (x + index)%len(dic)
        answer += dic[a]
        
    return answer