def solution(sequence, k):
    answer = []
    
    for i in range(len(sequence)):
        if sequence[i]==k:
            return [i,i]
    
    count = 0
    interval_sum = 0
    end = 0

    # start를 차례대로 증가시키며 반복
    for start in range(len(sequence)):
        # end를 가능한 만큼 이동시키기
        while interval_sum < k and end < len(sequence):
            interval_sum += sequence[end]
            end += 1
        # 부분합이 m일 때 카운트 증가
        if interval_sum == k:
            answer.append((start,end-1,end-1-start))
        
        interval_sum -= sequence[start]
    
    if len(answer)==1:
        return [answer[0][0],answer[0][1]]
    else:
        answer.sort(key = lambda x : x[2])
        return [answer[0][0],answer[0][1]]